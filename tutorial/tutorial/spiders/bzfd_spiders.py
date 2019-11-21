import scrapy
import datetime
 
class BuzzFeedSpider(scrapy.Spider):
    name = "bzfd"
 
    def start_requests(self):
        urls = [
            'https://www.buzzfeed.com/world.xml'
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
        filename = '../bzfd-news/bzfd-raw/buzzfeed-news-%s.html' % ts
        with open(filename, 'wb') as f:
            f.write(response.body)