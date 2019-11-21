import scrapy
import datetime
 
class BBCSpider(scrapy.Spider):
    name = "bbc"
 
    def start_requests(self):
        urls = [
            'http://feeds.bbci.co.uk/news/rss.xml',
            'http://feeds.bbci.co.uk/news/politics/rss.xml',
            'http://feeds.bbci.co.uk/news/business/rss.xml',
            'http://feeds.bbci.co.uk/news/health/rss.xml',
            'http://feeds.bbci.co.uk/news/education/rss.xml',
            'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml',
            'http://feeds.bbci.co.uk/news/technology/rss.xml',
            'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml',
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
        filename = '../bbc-news/bbc-raw/bbc-news-%s.html' % ts
        with open(filename, 'wb') as f:
            f.write(response.body)