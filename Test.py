# ---coding:utf-8---
import os
import shutil

s = os.sep
movieRoot = "E:" + s + u"IMDB" + s


# filename = u"007大战皇家赌场.Casino.Royale.2006.BDRip.x264.2Audio.AAC.miniSD-TLF.mkv"
# i = filename.find(".")
# name = filename[:i]
# os.mkdir(movieRoot+name)
# shutil.move(movieRoot+filename, movieRoot+name)


for filename in os.listdir(movieRoot):
    if os.path.isfile(movieRoot+filename):
        i = filename.find(".")
        name = filename[:i]
        os.mkdir(movieRoot+name)
        shutil.move(movieRoot+filename, movieRoot+name)