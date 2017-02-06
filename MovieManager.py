#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : t_zhehang
# Data : 17-1-27

from __future__ import division
from Movie import Movie
from DoubanManager import DoubanManager
import os
import string
import json
import pandas as pd
movieSizeFilter = 0.1


class MovieManager:


    def __init__(self):
        self.doubanManager = DoubanManager()
        self.movies = []
        self.moviesNotFound = ["小羊肖恩第一季", "小羊肖恩第二季", "大师",  "硬核亨利", "罪恶之城", "采访"]


    def getMovieFileNames(self, root):

        for i in os.listdir(root):
            temp = os.path.join(root, i)
            if os.path.isfile(temp):
                fileSize = round(os.path.getsize(temp) / (1024*1024*1024) , 1)
                if fileSize > movieSizeFilter:
                    temp = filter(None, i.split("."))

                    name = temp[0]
                    year = ""
                    source = ""
                    resolution = ""
                    fileType = temp[-1]
                    publish = temp[-2]
                    publish = self.get_publish(publish)

                    for j in range(1, len(temp)):
                        if self.check_contain_chinese(temp[j]):
                            name = name + "." + temp[j]
                        elif self.check_is_digit(temp[j]) and string.atoi(temp[j])>1900:
                            year = temp[j]
                        elif self.check_source(temp[j]):
                            source = temp[j]
                        elif self.check_is_digit(temp[j][0:-1]) and temp[j][-1].lower()=="p":
                            resolution = temp[j]

                    movie = Movie(name, year)
                    movie.setFileInfo(source, resolution, publish, fileType, fileSize)


                    doubanInfo = self.get_douban_info(root, name, year)

                    movie.setDoubanInfo(doubanInfo[0], doubanInfo[1], doubanInfo[2], doubanInfo[3], doubanInfo[4])

                    self.movies.append(movie)


                    # print(name+ " " + year + " " + source + " " + resolution + " " + publish + " " + fileType + " " + str(fileSize) + "G"  )
            else:
                self.getMovieFileNames(temp)


    def check_contain_chinese(self, check_str):

        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False


    def check_is_digit(self, check_str):

        nums = string.digits
        for ch in check_str:
            if ch not in nums:
                return False
        return True

    def check_source(self, check_str):

        source = ["bluray", "hdtv", "dvd", "dvdrip", "dvdscr", "web-dl" ,"bdrip", "brrip", "d9"]
        if check_str.lower() in source:
            return True
        return False

    def get_publish(self, publish):

        i = publish.find("-")
        if i > 0:
            return publish[i+1: ]
        elif publish.lower() not in ["ac3", "aac", "x264", "h264", "xvid"]:
            return publish
        else:
            return "Unknown"

    def get_douban_info(self, root, name, year):
        print("正在处理 " + str(len(self.movies)) + ":" + name.encode(encoding="UTF-8"))

        if name.encode(encoding="UTF-8") not in self.moviesNotFound:

            if os.path.exists(os.path.join(root, name + ".json")):
                html = open(os.path.join(root, name + ".json")).read()
                hjson = json.loads(html)

                if not hjson["year"] == year.encode(encoding="UTF-8"):

                    html = self.get_dioubanInfoJson(root, name, year)
                    hjson = json.loads(html)

            else:

                html = self.get_dioubanInfoJson(root, name, year)
                hjson = json.loads(html)

            directors = ""
            for d in hjson["directors"]:
                if directors == "":
                    directors = d["name"]
                else:
                    directors = directors + "/" + d["name"]

            actors = ""
            for d in hjson["casts"]:
                if actors == "":
                    actors = d["name"]
                else:
                    actors = actors + "/" + d["name"]

            rating = hjson["rating"]["average"]
            ratings_count = hjson["ratings_count"]
            alt = hjson["alt"]
            return [directors, actors, rating, ratings_count, alt]



        return ["", "", "", "", ""]


    def get_dioubanInfoJson(self, root, name, year):

        html = self.doubanManager.getJsonInfoFromNameAndYear(name, year)

        if html != "":
            output = open(os.path.join(root, name + ".json"), "w")
            output.write(html)
            output.close()

        return html




    def save_to_file(self, root):
        data = []
        for movie in self.movies:
            data.append(movie.getMovieInfo())

        df = pd.DataFrame(data, columns=["影片", "年份", "片源", "分辨率", "发布方", "文件类型", "文件大小", "导演", "主演", "豆瓣评分", "评分人数", "豆瓣链接"])
        df.to_csv(root + "test.csv", encoding="utf-8", index=False)


