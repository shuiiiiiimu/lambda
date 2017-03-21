# -*- coding: utf-8 -*-
import time

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DrawingPipeline(object):
    def process_item(self, item, spider):
        item['name'] = spider.name
        item['deadts'] = time.mktime(time.strptime(item['deadline'], '%Y-%m-%d %H:%M'))
        return item
