#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : t_zhehang
# Data : 17-1-24


class Movie:

    def __init__(self, name, year):

        self.name = name
        self.year = year


    def setFileInfo(self, source, resolution, publish, fileType, fileSize):

        self.source = source
        self.resolution = resolution
        self.publish = publish
        self.fileType = fileType
        self.fileSize = fileSize


    def setDoubanInfo(self, directors, actors,  genres, countries, durations, rating, ratings_count, alt):

        self.directors = directors
        self.actors = actors
        self.genres = genres
        self.countries = countries
        self.durations = durations
        self.rating = rating
        self.ratings_count = ratings_count
        self.alt = alt


    def getMovieInfo(self):


        return [self.name, self.year, self.source, self.resolution, self.publish, self.fileType, self.fileSize,
                self.directors, self.actors, self.genres, self.countries, self.durations, self.rating,
                self.ratings_count, self.alt]


    def getMovieInfoName(self):

        return ["影片", "年份", "片源", "分辨率", "发布方", "文件类型", "文件大小",
                "导演", "主演", "类型", "制片国家", "片长", "豆瓣评分", "评分人数", "豆瓣链接"]


if __name__ == "__main__":

    m = Movie("简洁", "2015")
    s = m.getMovieInfoName()
    print s