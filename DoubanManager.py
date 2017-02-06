#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : t_zhehang
# Data : 17-1-31
import urllib2
import json
import time
import string

class DoubanManager:
    searchPrefix = r"https://api.douban.com/v2/movie/search?q="
    subjectPrefix = r"https://api.douban.com/v2/movie/subject/"

    def __init__(self):
        self.waitTime = 8

    def getJsonInfoFromNameAndYear(self, name, year):

        movieId = self.getIdFromNameAndYear(name, year)
        if not movieId:
            print("搜索失败：" + name.encode(encoding="UTF-8"))
            return ""

        subjectUrl = DoubanManager.subjectPrefix + movieId.encode(encoding="UTF-8")

        try:
            time.sleep(self.waitTime)
            html = urllib2.urlopen(subjectUrl).read()
            return html

        except Exception as e:
            print e
            print("获取失败：" + name.encode(encoding="UTF-8") + " " + movieId.encode(encoding="UTF-8"))
            return ""

    def getIdFromNameAndYear(self, name, year):

        searchUrl = DoubanManager.searchPrefix + name.encode(encoding="UTF-8")
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

        if  string.atoi(year2) - string.atoi(year1)<= 1:
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

    doubanManager = DoubanManager()
    title = u"大师"
    year = u"2012"
    print(doubanManager.getJsonInfoFromNameAndYear(title, year))

    # for i in range(100):
    #     print(doubanManager.getJsonInfoFromName(title, ))
