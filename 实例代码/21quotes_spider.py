import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]
    # default callback method
    def parse(self, response):
        #                       CSS Selector
        for quote in response.css('div.quote'):
            #  yield  字典
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }
        # ook for a link to the next page and schedule another request using the same parse method as callback.
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)