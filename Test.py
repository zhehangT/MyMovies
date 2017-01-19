#---coding:utf-8---

import urllib2
import json
import string#后面处理页要用到

url = r'https://api.douban.com/v2/movie/subject/3434070'



print 'begin...'

try:
    html = urllib2.urlopen(url).read()
    hjson = json.loads(html)
    print hjson['title']

except Exception as e:
    print e


print 'over'
