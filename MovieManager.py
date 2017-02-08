#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : t_zhehang
# Data : 17-1-27

from __future__ import division
from Movie import Movie
from DoubanApiManager import DoubanApiManager
import os
import string
import pandas as pd
movieSizeFilter = 0.1


class MovieManager:


    def __init__(self):
        self.doubanManager = DoubanApiManager()
        self.movies = []


    def getMovieFromFileNames(self, root):

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
                    movie.setFileInfo(source, resolution, publish, fileType, str(fileSize)+"G")

                    print("正在处理 " + str(len(self.movies)) + ":" + name.encode(encoding="UTF-8"))
                    doubanInfo = self.doubanManager.getDoubanInfoFromNameAndYear(root, name, year)

                    movie.setDoubanInfo(doubanInfo[0], doubanInfo[1], doubanInfo[2], doubanInfo[3],
                                        doubanInfo[4], doubanInfo[5], doubanInfo[6], doubanInfo[7])

                    self.movies.append(movie)


                    # print(name+ " " + year + " " + source + " " + resolution + " " + publish + " " + fileType + " " + str(fileSize) + "G"  )
            else:
                self.getMovieFromFileNames(temp)


    # 判断字符串是否全部为中文字符(提取电影的中文名)
    def check_contain_chinese(self, check_str):

        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

    # 判断字符串是否为数字(提取电影的年份)
    def check_is_digit(self, check_str):

        nums = string.digits
        for ch in check_str:
            if ch not in nums:
                return False
        return True

    # 提取电影的片源
    def check_source(self, check_str):

        source = ["bluray", "hdtv" ,"hdrip", "dvd", "dvdrip", "dvdscr", "web-dl" ,"bdrip", "brrip", "d9", "d5"]
        if check_str.lower() in source:
            return True
        return False

    # 提取电影的发布方
    def get_publish(self, publish):

        i = publish.find("-")
        if i > 0:
            return publish[i+1: ]
        elif publish.lower() not in ["ac3", "aac", "x264", "h264", "xvid"]:
            return publish
        else:
            return "Unknown"

    # 保存电影信息为csv文件
    def saveToFile(self, root):

        self.doubanManager.saveMoviesNotFound()
        data = []
        for movie in self.movies:
            data.append(movie.getMovieInfo())

        df = pd.DataFrame(data, columns=movie.getMovieInfoName())
        df.to_csv(root + "test.csv", encoding="utf-8", index=False)


