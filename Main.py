#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : t_zhehang
# Data : 17-1-24

from MovieManager import MovieManager
import os

s = os.sep
# movieRoot = "E:" + s + u"电影" + s
movieRoot = "E:" + s + u"IMDB" + s


if __name__ == "__main__":

    movieManager = MovieManager()
    movieManager.getMovieFromFileNames(movieRoot)
    movieManager.saveToFile(movieRoot)


    print("\nGet All Movie File Names")


