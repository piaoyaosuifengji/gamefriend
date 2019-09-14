# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetmyfavoritepagesItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()              #标题
    website = scrapy.Field()            #主站
    url = scrapy.Field()                #具体url  
    language = scrapy.Field()           # 文章的语言
    readFlag = scrapy.Field()           # 1表示已经阅读，0表示没有
    PublicationDate = scrapy.Field()    # 文章发布日期
    text = scrapy.Field()               # 文本概要
    
    
     
def initFavoritePageItem():
    page = GetmyfavoritepagesItem()

    page['title'] = ""
    page['website'] = ""
    page['url'] = ""
    page['language'] = ""
    page['readFlag'] = ""
    page['PublicationDate'] = ""
    page['text'] = ""

    return page