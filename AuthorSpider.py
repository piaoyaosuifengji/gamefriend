import scrapy


class AuthorSpider(scrapy.Spider):
    #  class scrapy.spiders.CrawlSpider  是另外通用的爬虫类
    name = 'author'

    start_urls = ['http://quotes.toscrape.com/']

    #系统会自动过滤掉访问过的页面： DUPEFILTER_CLASS  类中可以设置该选项 
    def parse(self, response):
        # follow links to author pages
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)

        # follow pagination links
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }