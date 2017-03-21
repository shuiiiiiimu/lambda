# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DrawingItem(scrapy.Item):
    current = scrapy.Field()
    deadline = scrapy.Field()
    deadts = scrapy.Field()
    name = scrapy.Field()
    pass
