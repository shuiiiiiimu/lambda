# -*- coding: utf-8 -*-

import scrapy
from scrapy import signals
import re
from draw.items import DrawingItem


class A163Spider(scrapy.Spider):
    name = "a163"
    allowed_domains = ["caipiao.163.com"]
    start_urls = ['http://caipiao.163.com/order/3d/#from=syks']

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(A163Spider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signals.spider_closed)
        return spider


    def spider_closed(self, spider):
    	print('----------------close------------', spider.name)
    	self.running_crawlers.remove(spider)
    	if not self.running_crawlers:
    		reactor.stop()


    def parse(self, response):
        item = DrawingItem()
        item['current'] = int(response.xpath('//*[@id="bet_period"]/text()').extract()[0])
        deadline = response.xpath('//*[@id="bet_time"]/text()').extract()[0]
        item['deadline'] = str(re.findall(r"(\d+-\d+-\d+\s\d+:\d+)", deadline)[0])
        yield item
