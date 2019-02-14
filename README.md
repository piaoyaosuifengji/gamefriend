# scrapyMyPage
create


在vscode中配置python3： 

<!-- 命令查看Python3安装路径
python3
import sys
print sys.path
['', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/home/jty/.local/lib/python3.6/site-packages', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages']

<!-- 将  /usr/lib/python3.6  写入  用户设置中 -->
  <!-- 添加python3的路径   file->首选项->settings->在“python.pythonPath”中写入 -->


抓取项目怎么安排呢？
    1：先把数据抓取下来再说？
    2：再进行翻译？










<!-- 安装 -->
 ai python3-scapy

<!-- # 创建一个 scrapy 项目 -->
在目录：/home/jty/git/scrapyMyPage/getMyFavoritePages
scrapy startproject getMyFavoritePages


# 假设你已经写了一个爬虫类 quotes（类名）  了，运行方法：
scrapy crawl spiderForShortPageMsg
<!-- 将所有爬虫运行中的debug信息及抓取到的信息打印在all.log中 -->
scrapy crawl spiderForShortPageMsg  -s LOG_FILE=all.log








