import scrapy


class LinkedSpiderSpider(scrapy.Spider):
    name = 'linked_spider'
    allowed_domains = ['linkedin.com']
    start_urls = ['http://linkedin.com/']

    def parse(self, response):
        pass
