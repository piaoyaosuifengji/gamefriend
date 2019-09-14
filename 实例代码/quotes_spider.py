import scrapy












class QuotesSpider(scrapy.Spider):
    name = "quotes"  #给spider命名，一个project 下是唯一的

    # 必须返回一个可迭代的 Request ：比如list 或者 generator function
    # spider会以此开始爬取内容
    # 随后的请求将从这些初始请求中依次生成。

    # start_requests 也可以不自己写，而用一个urls变量来替代，这样系统就
    # 会调用默认的 start_requests 函数了
    '''
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    '''

    # 替代 start_requests
    # 默认情况下，只会抓取俩个page页面的数据
    # 如果想要抓取整个网站的数据，就必须对网页的链接link对象进行提取
    # 你需要找到 <li>对象
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        # 'http://quotes.toscrape.com/page/2/',
    ]
    # 版本2  提取其中的数据 不继续抓取链接网页
    '''
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
    '''
    '''
    # 版本3  提取其中的数据 后，继续抓取链接网页
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
         
        if next_page is not None:
            
            # 这里的 next_page = /page/2/
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            
             # 省略 response.urljoin(next_page) 的方法，使用相对路径
            yield response.follow(next_page, callback=self.parse)
    '''

    #版本4：简化寻找链接的代码
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
        # 
        # for href in response.css('li.next a::attr(href)'):
        # 或者： （效果一样）
        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)






    


        # a method that will be called to handle the response downloaded for each of the requests made.
    #  response 是一个 TextResponse 对象 保存这爬取的实际内容

    # 版本1：只是下载html文件
    '''
    
    def parse(self, response):

        # print(response.url.split("/"))
        # print("\n")
        # print("\n")

        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
    '''