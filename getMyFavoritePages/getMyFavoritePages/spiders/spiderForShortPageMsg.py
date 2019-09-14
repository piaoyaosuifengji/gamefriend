#! python3
# -- coding: utf-8
import scrapy
import logging
import re

from scrapy.http import Request
from getMyFavoritePages.items import GetmyfavoritepagesItem,initFavoritePageItem
# from jobboleSpider.utils.common import get_md5
# import datetime
# from scrapy.loader import ItemLoader

# from boilerpipe.extract import Extractor

class AuthorSpider(scrapy.Spider):
    #  class scrapy.spiders.CrawlSpider  是另外通用的爬虫类
    name = 'spiderForShortPageMsg'


    start_urls = [ 
        # 'https://lobste.rs/',
        # 'https://readwrite.com/',
        # 'https://news.ycombinator.com/',
        # 'https://www.ostechnix.com/',
        # 'https://www.infoworld.com/',
        'https://dzone.com/',
    ]
    #系统会自动过滤掉访问过的页面： DUPEFILTER_CLASS  类中可以设置该选项 
    def parse(self, response):
        # logging.warning("parse : current url is:"+response.url  )
        # logging.warning("\n" )


        
        # follow links to author pages
        # for href in response.css('.author + a::attr(href)'):
        #     yield response.follow(href, self.parse_author)
        #     print(href)

 
        if response.url == "https://readwrite.com/":
            # for href in response.xpath('//h2/a'):
            # or :
            # for href in response.xpath('//article/div/div[2]/header/h2/a'):     # xpath  成功
            #     yield {
            #         'text': href.css('a::text').extract_first(),
            #         'href': href.css('a::attr(href)'), 
                # }
            pass

        elif response.url == "https://lobste.rs/":
            # for href in response.xpath("//div/div[2]/span[1]/a[@class='u-url']"):     #   ok
            # # for href in response.xpath('//div/span[1]/a'):     #https://lobste.rs/
            #     yield {
            #         'text': href.css('a::text').extract(),
            #         # 'text': href.css('a::text').extract_first(),
            #         # 'tmp': '\n',
            #         'href': href.css('a::attr(href)'), 
            #     }
            pass
        elif response.url == "https://news.ycombinator.com/":
            # for href in response.xpath("//table[@class='itemlist']/tr/td[3]"):     #   ok
            #     yield {
            #         'text': href.xpath("./a").css('a::text').extract_first(),
            #         'href': href.xpath("./a").css('a::attr(href)').extract_first(),
            #     }
            pass
        elif response.url == "https://www.ostechnix.com/":
            # for href in response.xpath("//div[@class='post-row']//article/div"):     #   ok
            #     yield {
            #         'title': href.xpath("./h2").css('a::text').extract_first(),
            #         'text': href.xpath("./div[@class='entry excerpt entry-summary']").css('p::text').extract_first(),
            #         'href': href.xpath("./h2").css('a::attr(href)').extract_first(),
            #     }
            pass
        elif response.url == "https://www.infoworld.com/":
            # for href in response.xpath("//div[@class='main-col']/div[@class='item']/h4/a"):     #   ok
            #     yield {
            #         'text': href.css('a::text').extract_first(),
            #         'href': href.css('a::attr(href)').extract_first(),
            #     }
            pass
        elif response.url == "https://dzone.com/":

            yield response.follow(response.url, self.parse_dzone_com)



    def atricalClean(self, str_):
        

        tmpstr =str_

        
        def isDirty(tmpstr):
            start = tmpstr.find('<')
            end = tmpstr.find('>')
            # print(start)
            # print(end)
            if start != -1 and end != -1 and end > start:
                return 1
            return 0

        while isDirty(tmpstr) == 1:
            # print("isDirty: ")
            start = tmpstr.find('<')
            end = tmpstr.find('>')
            dropStr = tmpstr[start:end +1]
            tmpstr = tmpstr.replace(dropStr, "",1)


        tmpList = ["\\xa0",
                    "\\n",
                    # "\\n",
                    ]
        for i in range(len(tmpList)):
            if tmpList[i] == "\\n":
                tmpstr=tmpstr.replace(tmpList[i], '\n')
            else:
                tmpstr=tmpstr.replace(tmpList[i], " " )
        start = 2
        # end = len(tmpstr) 
        tmpstr=tmpstr[start:-2]
        return tmpstr

    def parse_dzone_com_artical(self, response):

        # print("parse_dzone_com_artical: start ")

        # for href in response.xpath("//li[@class='col-md-3 column col-sm-4 col-xs-6']/div[@class='titles']"):     #   ok
        pageItem  = initFavoritePageItem()
        # page['title'] = ""
        # page['website'] = ""
        pageItem['url'] =  response.url
        # page['language'] = ""
        # page['readFlag'] = ""
        # page['PublicationDate'] = ""

        # print(pageItem['url'])


        hObj = response.xpath("//h1[@class='article-title']")[0] 
        # titleStr = 
        # pageItem['title'] = titleStr.strip()
        pageItem['title'] = hObj.css('::text').get().strip()
        
        articalNode = response.xpath("//div[@class='content-html']")[0]
        for href in articalNode.xpath("./*") :     #   ok

            
            # print( href.xpath('./*/text()').get() )
            
            # print( href.xpath('./text()').get() )
            # 打印节点的html代码
            # print( href.getall())
            # print( re.sub("<*>", "", href.getall(), count=0) )

            # print( href.getall())
            strs1  = self.atricalClean(  str( href.getall()))
            
            # strs11 = "".join(strs1.split())
            print( strs1)
            

        yield pageItem



    def parse_dzone_com(self, response):

        # logging.warning("parse : current url is:"+response.url  )
        logging.debug("parse : current url is:"+response.url  )

        for href in response.xpath("//li[@class='col-md-3 column col-sm-4 col-xs-6']/div[@class='titles']"):     #   ok
            for tmpDiv in href.xpath("./div/h3/a"):     #   ok

                pageItem  = initFavoritePageItem()
                # page['title'] = ""
                # page['website'] = ""
                pageItem['url'] =  "https://dzone.com"+tmpDiv.css('a::attr(ng-href)').extract_first()
                # page['language'] = ""
                # page['readFlag'] = ""
                # page['PublicationDate'] = ""

                # print(pageItem['url'])
                pageItem['title'] = tmpDiv.css('a::text').extract_first()


                # yield {
                #     'text': tmpDiv.css('a::text').extract_first(),
                #     'href': tmpDiv.css('a::attr(ng-href)').extract_first(),
                # }
                # yield pageItem


                if pageItem['url'] == "https://dzone.com/articles/the-6-best-slack-alternatives-for-effective-projec":
                    yield response.follow(pageItem['url'], self.parse_dzone_com_artical)


                pass
            for tmpDiv in href.xpath("./h3/a"):     #   ok
                # yield {
                #     'text': tmpDiv.css('a::text').extract_first(),
                #     'href': tmpDiv.css('a::attr(ng-href)').extract_first(),
                # }
                # pass
                pageItem  = initFavoritePageItem()
                # page['title'] = ""
                # page['website'] = ""
                pageItem['url'] =  "https://dzone.com"+tmpDiv.css('a::attr(ng-href)').extract_first()
                # page['language'] = ""
                # page['readFlag'] = ""
                # page['PublicationDate'] = ""

                pageItem['title'] = tmpDiv.css('a::text').extract_first()
                # yield pageItem
                if pageItem['url'] == "https://dzone.com/articles/multi-team-backlog-refinement":
                    yield response.follow(pageItem['url'], self.parse_dzone_com_artical)

 


    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }















