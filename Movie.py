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

    def setDoubanInfo(self, directors, actors, rating, ratings_count, alt):

        self.directors = directors
        self.actors = actors
        self.rating = rating
        self.ratings_count = ratings_count
        self.alt = alt

    def getMovieInfo(self):

        return [self.name, self.year, self.source, self.resolution, self.publish, self.fileType, self.fileSize,
                self.directors, self.actors, self.rating, self.ratings_count, self.alt]
