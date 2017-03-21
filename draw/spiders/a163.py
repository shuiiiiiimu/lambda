# -*- coding: utf-8 -*-

import scrapy
import re
from draw.items import DrawingItem


class A163Spider(scrapy.Spider):
    name = "a163"
    allowed_domains = ["caipiao.163.com"]
    start_urls = ['http://caipiao.163.com/order/3d/#from=syks']

    def parse(self, response):
        item = DrawingItem()
        item['current'] = int(response.xpath('//*[@id="bet_period"]/text()').extract()[0])
        deadline = response.xpath('//*[@id="bet_time"]/text()').extract()[0]
        item['deadline'] = str(re.findall(r"(\d+-\d+-\d+\s\d+:\d+)", deadline)[0])
        yield item
