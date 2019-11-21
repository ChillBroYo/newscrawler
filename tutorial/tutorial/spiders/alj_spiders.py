import scrapy
import datetime
 
class AljSpider(scrapy.Spider):
    name = "alj"
 
    def start_requests(self):
        urls = [
            'https://www.aljazeera.com/xml/rss/all.xml'
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
        filename = '../alj-news/alj-raw/alj-news-%s.html' % ts
        with open(filename, 'wb') as f:
            f.write(response.body)