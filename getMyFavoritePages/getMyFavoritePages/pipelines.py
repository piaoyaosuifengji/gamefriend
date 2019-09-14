# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class GetmyfavoritepagesPipeline(object):
    def process_item(self, item, spider):


        print("url is :"+item['url'])
        print("title  is :"+item['title'])
        print(" ")

        DropItem("end chuli  %s" % item)
        # return item
