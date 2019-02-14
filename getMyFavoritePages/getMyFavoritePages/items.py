# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetmyfavoritepagesItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    website = scrapy.Field()            #主站
    url = scrapy.Field()                #具体url  
    language = scrapy.Field()           # 
    language = scrapy.Field()           # 
    
    
     
