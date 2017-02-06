# ---coding:utf-8---

import json

a = open(u"E:\电影\一个叫欧维的男人决定去死\一个叫欧维的男人决定去死.json").read()
hjson = json.loads(a)
actors = ""
for d in hjson["casts"]:
    if actors == "":
        actors = d["name"]
    else:
        actors = actors + "/" + d["name"]

print(actors)

print(hjson["rating"]["average"])