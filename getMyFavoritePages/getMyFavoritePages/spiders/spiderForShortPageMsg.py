#!/usr/lib/python3.6
import scrapy
import logging

class AuthorSpider(scrapy.Spider):
    #  class scrapy.spiders.CrawlSpider  是另外通用的爬虫类
    name = 'spiderForShortPageMsg'


    start_urls = [ 
        'https://lobste.rs/',
        'https://readwrite.com/',
        'https://news.ycombinator.com/',
        'https://www.ostechnix.com/',
        'https://www.infoworld.com/',
        'https://dzone.com/',
    ]
    #系统会自动过滤掉访问过的页面： DUPEFILTER_CLASS  类中可以设置该选项 
    def parse(self, response):
        logging.warning("parse : current url is:"+response.url  )
        logging.warning("\n" )


        
        # follow links to author pages
        # for href in response.css('.author + a::attr(href)'):
        #     yield response.follow(href, self.parse_author)
        #     print(href)

        # response.xpath('//div[@id="images"]').css('img')
        # for href in response.css('.(link h-cite u-repost-of) + a::attr(href)'):
        # for href in response.xpath('//div[@class=link h-cite u-repost-of]').css('a'): 
        # for href in response.xpath('//ol/div//a'):  #https://lobste.rs/
        # for href in response.xpath('//article//a/text()'):     #https://readwrite.com/

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
            for href in response.xpath("//li[@class='col-md-3 column col-sm-4 col-xs-6']/div[@class='titles']"):     #   ok
                for tmpDiv in href.xpath("./div/h3/a"):     #   ok
                    yield {
                        'text': tmpDiv.css('a::text').extract_first(),
                        'href': tmpDiv.css('a::attr(ng-href)').extract_first(),
                    }
                    pass
                for tmpDiv in href.xpath("./h3/a"):     #   ok
                    yield {
                        'text': tmpDiv.css('a::text').extract_first(),
                        'href': tmpDiv.css('a::attr(ng-href)').extract_first(),
                    }
                    pass











    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }















