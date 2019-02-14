







# ：先不要管代码，先学习下怎么使用再说

    1:先试着抓取你常浏览的网页数据再说-----------目前倒是基本知道该怎么使用了   （ok）
    2：将数据抓取后进行本地存储：学习使用 Items 和 Item Pipeline
        在Item Pipeline 中实现以下功能：
        a：和本地数据（最好是放入数据库当中）进行比较，重复的丢掉

        b：不重复的就写入本地存储，并生成一个新的增量数据列表---这是你需要阅读的文章
            将  增量数据列表  生成一个csv 文件（或者其他的），方便以后生成html，进行阅读

    终极目标：看看是否能够利用 scrapy 抓取各种 web 翻译的信息  ----其实有点舍本逐末了







# scrapy的配置文件分为：
 1   /etc/scrapy.cfg  (system-wide),
 2   ~/.config/scrapy.cfg   ~/.scrapy.cfg ($HOME) (user-wide) 
 3   scrapy.cfg inside a scrapy project’s root  

# environment variables：
    SCRAPY_SETTINGS_MODULE (see Designating the settings)
    SCRAPY_PROJECT
    SCRAPY_PYTHON_SHELL (see Scrapy shell)



# 查看版本：
scrapy -v

# 创建一个 scrapy 项目
                        
scrapy startproject mingyan
scrapy startproject test1





# 假设你已经写了一个爬虫类了，运行方法：
scrapy crawl quotes
scrapy crawl spiderForShortPageMsg
# 将数据放入文件中
scrapy crawl quotes -o quotes.json
# 出于历史原因，输出时，Scrapy将一个给定的文件进行数据的附加  而不是覆盖其内容。如果您在第二次运行该命令两次而没有在第二次之前删除该文件，那么最终会得到一个损坏的JSON文件。


# 数据解析：
scrapy shell 'http://quotes.toscrape.com/page/1/'
On Windows,
scrapy shell "http://quotes.toscrape.com/page/1/"


# 在shell 中可以查看解析结果：

response.css('title')  #返回所有元素
：
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]


response.css('title::text').extract()  #只返回 title 的文本
：
['Quotes to Scrape']

# # extract() 返回一个列表：
# The SelectorList class is a subclass of the builtin list class, which provides a few additional methods.
             # 元素名.类名：：text
response.css('title::text').extract_first()  #代码更
或者
response.css('title::text')[0].extract()
：
'Quotes to Scrape'
# 同时满足   就是 div.tags   下的  a.tag::text
tags = quote.css("div.tags a.tag::text").extract()
['change', 'deep-thoughts', 'thinking', 'world']




>>> for quote in response.css("div.quote"):
...     text = quote.css("span.text::text").extract_first()
...     author = quote.css("small.author::text").extract_first()
...     tags = quote.css("div.tags a.tag::text").extract()
...     print(dict(text=text, author=author, tags=tags))
{'tags': ['change', 'deep-thoughts', 'thinking', 'world'], 'author': 'Albert Einstein', 'text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'}
{'tags': ['abilities', 'choices'], 'author': 'J.K. Rowling', 'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”'}
    ... a few more of these, omitted for brevity （省略）
>>>



# 提取链接对象：
response.css('li.next a').extract_first()
'<a href="/page/2/">Next <span aria-hidden="true">→</span></a>'

>>> response.css('li.next a::attr(href)').extract_first()
'/page/2/'


# 在命令行中传如参数：
scrapy crawl quotes -o quotes-humor.json -a tag=humor
# 在代码中  可以用：
def start_requests(self):
    tag =getattr(self, 'tag', None)  获取
# 或者：
scrapy.Request('http://www.example.com/categories/%s' % self.category)


# A shortcut to TextResponse.selector.xpath(query):
response.xpath