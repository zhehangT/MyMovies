#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : t_zhehang
# Data : 17-1-23

from bs4 import BeautifulSoup
import urllib2

class Award:

    def __init__(self, text):
        self.categories = []
        first = True
        text = filter(None, text.split('\n\n\n'))
        for t in text:
            if t:
                t = filter(None, t.split('\n'))
                if first:
                    self.name = t[0]
                    self.year = t[1]
                    first = False
                elif len(t) == 1:
                    category = Category(t[0])
                    self.addCategory(category)
                else:
                    category = Category(t[0], t[1])
                    self.addCategory(category)

    def addCategory(self, category):

        self.categories.append(category)


class Category:

    def __init__(self, name, winner=''):
        self.name = name
        self.winner = winner


class Text:

    def __init__(self, url):

        self.text = []
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        temp = soup.find_all('div', attrs={'class': 'awards'})

        for t in temp:
            self.text.append(t.get_text())


if __name__ == '__main__':
    print('get start')

    # test = u'\n\n\n第74届金球奖\n(2017)\n\n\n\n电影类 最佳音乐/喜剧片\n\n\n\n电影类 音乐/喜剧片最佳男主角\n瑞恩·高斯林\n\n\n电影类 音乐/喜剧片最佳女主角\n艾玛·斯通\n\n\n电影类 最佳导演\n达米安·沙泽勒\n\n\n电影类 最佳编剧\n达米安·沙泽勒\n\n\n电影类 最佳原创配乐\n\n\n\n电影类 最佳原创歌曲\n\n\n'
    # award = Award(test)


    url = r'https://movie.douban.com/subject/25934014/awards/'
    text = Text(url)

    awards = []
    for t in text.text:
        awards.append(Award(t))


    print('get over')