#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : t_zhehang
# Data : 17-1-18


from bs4 import BeautifulSoup
import urllib2

url = r'https://movie.douban.com/subject/25934014/awards/'
html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())
print(soup.title)

aa = soup.find_all('div',attrs={'class':'awards'})

for a in aa:
    s = a.get_text()
    print(a.get_text())