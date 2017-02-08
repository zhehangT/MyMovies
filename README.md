# 简介

每个人的观影生涯总会遇到很多障碍。比如：
最近心情郁闷，有什么电影值得推荐？
哪里可以下载到观影体验最好的电影资源？
这部电影有哪些值得细细解读的地方？
也许有一天，可以有一个人工智能能够帮助我们解答所有问题。

电影《一一》里说，电影发明以后，人类生命延长了三倍。
所以这个项目奉献给对电影最诚挚的热爱。

MyMovies将经历三个阶段。

**非智能阶段**
这个阶段的MyMovies可以作为本地电影视频的管理工具以及网络信息的获取工具。但是人本身是主要决策者。
作为本地电影视频的管理工具，MyMovies可以知道本地已经下载了哪些电影视频，并获取这些视频的详细信息。
作为网络信息的获取工具，MyMovies可以从网络上获取各种电影信息，构建电影的知识库。电影的知识库主要包含几个方面。首先是电影的详细信息，包含导演，主演，豆瓣评分，IMDB评分等等。其次是各种榜单的信息，包括历年三大电影节的获奖电影，奥斯卡获奖电影，法国《电影手册》年度十佳，英国《视与听》年度十佳，日本《电影旬报》年度十佳等等。然后是著名导演和著名演员的电影集。最后是可以从资源站爬取电影的种子资源或磁力链资源。

MyMovies将长期处于这个阶段。

**半智能阶段**
这个阶段的MyMovies具备简单的智能水平。
MyMovies能够根据使用者的观影纪录和电影的知识库，完成简单的电影推荐功能。
MyMovies能够自动辨别网络资源的优劣，完成电影的下载和更新。

**智能阶段**
MyMovies自己写影评？与使用者直接讨论？
请尽情想象。


# 日志
### beta 0.1
**完成功能**
1. 完成了电影视频文件的解析。可以从中提取影片名称，年份，片源，分辨率，发布方，文件类型，文件大小。
2. 通过豆瓣API爬取电影信息。可以获得导演，主演，类型，制片国家，豆瓣评分，评分人数，豆瓣链接。
3. 将上述信息保存为excel文件。
![excel文件示例](http://oeaxm0g1o.bkt.clouddn.com/demo.png "excel文件示例")

**存在问题**
1. 电影视频文件的解析必须要求名称符合正规命名规则。不符合规则无法正确解析。
    > *勇士.Warrior.2011.1080p.BluRay.H264.AAC-RARBG.mp4*
为正规命名规则，包含中文名，英文名，年份，分辨率，视频编码，音频编码以及资源发布方。

    > *Warrior.2011.勇士.双语字幕.HR-HDTV.AC3.1024X576.x264-人人影视制作.mkv*
    > *[勇士]Warrior.2011.BluRay.1080p.x264.DTS-CnSCG[中英字幕/11.2G].mkv*
    > *[12.12][2011年美国动作体育][勇士][BD-RMVB][中英字幕].mvk*
均为非正规命名规则

2. 通过豆瓣API访问受限，大约每分钟只能发起10次http请求。无法大规模爬取电影信息。

3. 如果电影中文名称采用台湾译名，则无法从豆瓣获取正确的信息。
> 美食总动员的台湾译名为料理鼠王，很多网上下载的都以料理鼠王命名。

4.采用excel文件展示电影信息比较简陋。

**TODO**
1. 增强电影视频文件解析的鲁棒性，根据一些资源发布方的命名习惯，实现一定程度上的自动修正功能。
2. 用爬虫替换豆瓣API，实现大规模的电影信息爬取。
3. 即使通过台湾译名也能从豆瓣获取正确信息。
4. 设计展示界面，替换excel这种展示形式。
5. 设计数据结构和数据库，为构建本地电影知识库作准备。


