#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : t_zhehang
# Data : 17-1-31
import cPickle
import urllib2
import json
import time
import string
import os

class DoubanApiManager:

    searchPrefix = r"https://api.douban.com/v2/movie/search?q="
    subjectPrefix = r"https://api.douban.com/v2/movie/subject/"
    subjectPrefix2 = r"https://movie.douban.com/subject/"

    def __init__(self):
        self.waitTime = 8
        if os.path.exists("moviesNotFound.pkl"):
            f = open("moviesNotFound.pkl", "rb")
            self.moviesNotFound = cPickle.load(f)
            f.close()
        else:
            self.moviesNotFound = []


    def saveMoviesNotFound(self):

        if self.moviesNotFound:

            f = open("moviesNotFound.pkl", "wb")
            cPickle.dump(self.moviesNotFound, f)
            f.close()

            for movie in self.moviesNotFound:
                print("获取失败：" + movie[0] + " "
                      + movie[1] + " "
                      + DoubanApiManager.subjectPrefix2+movie[2])




    def getDoubanInfoFromNameAndYear(self, root, name, year):

        if not self.check_is_in_NotFound(name.encode(encoding="UTF-8"), year.encode(encoding="UTF-8")):

            if os.path.exists(os.path.join(root, name + ".json")):
                html = open(os.path.join(root, name + ".json")).read()
                hjson = json.loads(html)
                if not hjson["year"] == year.encode(encoding="UTF-8"):
                    html = self.get_info_json_from_name_and_year(root, name, year)


            else:

                html = self.get_info_json_from_name_and_year(root, name, year)

            if not html:
                return ["", "", "", "", "", "", "", ""]

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

            genres = ""
            for d in hjson["genres"]:
                if genres == "":
                    genres = d
                else:
                    genres = genres + "/" + d

            countries = ""
            for d in hjson["countries"]:
                if countries == "":
                    countries = d
                else:
                    countries = countries + "/" + d

            durations = ""

            rating = hjson["rating"]["average"]
            ratings_count = hjson["ratings_count"]
            alt = hjson["alt"]
            return [directors, actors, genres, countries, durations, rating, ratings_count, alt]

        return ["", "", "", "", "", "", "", ""]


    def check_is_in_NotFound(self, name, year):

        for movie in self.moviesNotFound:
            if name == movie[0] and self.check_year(movie[1], year):
                return True
        else:
            return False


    # 根据电影名称和年份获取豆瓣电影对应的json信息，获取失败返回None
    def get_info_json_from_name_and_year(self, root, name, year):

        movieId = self.get_id_from_name_and_year(name, year)
        if not movieId:
            print("搜索失败：" + name.encode(encoding="UTF-8"))
            return None

        subjectUrl = DoubanApiManager.subjectPrefix + movieId.encode(encoding="UTF-8")

        try:
            time.sleep(self.waitTime)
            html = urllib2.urlopen(subjectUrl).read()
            output = open(os.path.join(root, name + ".json"), "w")
            output.write(html)
            output.close()
            return html

        except Exception as e:
            print e
            # print("获取失败：" + name.encode(encoding="UTF-8") + " " + movieId.encode(encoding="UTF-8"))
            self.moviesNotFound.append([name.encode(encoding="UTF-8"), year.encode(encoding="UTF-8"), movieId.encode(encoding="UTF-8")])
            return None

    # 根据电影名称和年份获取豆瓣电影对应的id，获取失败返回None
    def get_id_from_name_and_year(self, name, year):

        searchUrl = DoubanApiManager.searchPrefix + name.encode(encoding="UTF-8")
        try:
            time.sleep(self.waitTime)
            html = urllib2.urlopen(searchUrl).read()
            hjson = json.loads(html)
            results = hjson["subjects"]
            for result in results:
                if self.get_only_chinese(name) == self.get_only_chinese(result["title"])\
                        and self.check_year(result["year"], year.encode(encoding="UTF-8")):
                    # print(result["title"])
                    return result["id"]

        except Exception as e:
            print e

        return None


    def check_year(self, year1, year2):

        if  string.atoi(year2) - string.atoi(year1) <= 1:
            return True
        else:
            return False


    def get_only_chinese(self, check_str):
        result = ""
        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                result += ch
        return result


if __name__ == "__main__":

    doubanManager = DoubanApiManager()
    title = u"大师"
    year = u"2012"
    print(doubanManager.get_info_json_from_name_and_year(title, year))

    # for i in range(100):
    #     print(doubanManager.getJsonInfoFromName(title, ))
