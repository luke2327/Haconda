# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HacondaPipeline(object):
    def process_item(self, item, spider):
        import time
        from datetime import datetime
        print 'action' + str(datetime.now())
        return item
