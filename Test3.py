#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : t_zhehang
# Data : 17-1-19

from bs4 import BeautifulSoup
import urllib2

# url = r'https://movie.douban.com/subject/25934014/awards/'
# html = urllib2.urlopen(url).read()

html = open('test.html').read()
soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())