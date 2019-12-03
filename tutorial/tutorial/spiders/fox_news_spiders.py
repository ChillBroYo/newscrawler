import scrapy
import datetime
 
class FoxNewsSpider(scrapy.Spider):
    name = "fox"
 
    def start_requests(self):
        urls = [
            'http://feeds.foxnews.com/foxnews/latest',
            'http://feeds.foxnews.com/foxnews/national',
            'http://feeds.foxnews.com/foxnews/world',
            'http://feeds.foxnews.com/foxnews/politics',
            'http://feeds.foxnews.com/foxnews/scitech',
            'http://feeds.foxnews.com/foxnews/health',
            'http://feeds.foxnews.com/foxnews/entertainment',
            'http://feeds.foxnews.com/foxnews/world'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        for post in response.xpath('//channel/item'):
            yield {
                'title' : post.xpath('title//text()').extract_first(),
                'description' : post.xpath('description//text()').extract_first(),
                'link': post.xpath('link//text()').extract_first(),
                'pubDate' : post.xpath('pubDate//text()').extract_first(),
            }
        ts = datetime.datetime.now().timestamp()
        filename = '../fox-news/fox-raw/fox-news-%s.html' % ts
        with open(filename, 'wb') as f:
            f.write(response.body)