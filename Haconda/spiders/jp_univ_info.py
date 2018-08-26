# -*- coding: utf-8 -*-

import scrapy
import time
import csv
import logging
from Haconda.items import HacondaItem

class JapanUnivInformationSpider(scrapy.Spider):
    name = "info_jp_jpss"
    start_urls = [
            "https://www.jpss.jp/ko/search/?tb=1&a%5Bnm%5D=&a%5Bfw%5D=&u%5Bfc%5D=&u%5Bdp%5D=%E6%83%85%E5%A0%B1&u%5Bac%5D=&a%5Bpf%5D=8-9-10-11-12-13-14-15-19-20&search=search",
            ]

    def start_requests(self):
        for link in self.start_urls:
            yield scrapy.Request(link, self.parse, dont_filter=True)

    def parse(self, response):
        print 'a'
        logging.info(response.status)
