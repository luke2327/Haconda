# -*- coding: utf-8 -*-

import scrapy
import time
import csv
import logging
from Haconda.items import HacondaItem

class JapanUnivInformationSpider(scrapy.Spider):
    name = "info_jp_accept_eju_list"
    start_urls = [
            "https://www.jasso.go.jp/ryugaku/study_j/eju/examinee/prearrival/uni_national.html",
            ]

    def start_requests(self):
        for link in self.start_urls:
            yield scrapy.Request(link, self.parse, dont_filter=True)

    def parse(self, response):
        for univ in\
        response.xpath('//div[@id="SearchResult"]/div'):
            item = HacondaItem()
            item['source'] = 'jpss.jp'
            try:
                item['location'] = univ.xpath('div[1]/div[1]/ul/li[2]/a[1]/text()').extract()[0]
                item['univ_type'] = univ.xpath('div[1]/div[1]/ul/li[2]/text()[2]').extract()[0]
                item['name'] = ' | '.join(univ.xpath('div[1]/div[1]/h3/a/span/text()').extract())
                item['undergraduate'] = univ.xpath('div[2]/ul/li/a/@title').extract()
                item['link'] = 'https://www.jpss.jp' +\
                        str(univ.xpath('div[1]/div[1]/h3/a/@href').extract()[0])

                if ',' in item['univ_type']:
                    item['univ_type'] = univ.xpath('div[1]/div[1]/ul/li[2]/text()[3]').extract()[0]
                    if ',' in item['univ_type']:
                        item['univ_type'] = univ.xpath('div[1]/div[1]/ul/li[2]/text()[4]').extract()[0]

                if 'Private' in item['univ_type']:
                    item['univ_type'] = 'Private'
                elif 'National' in item['univ_type']:
                    item['univ_type'] = 'National'
                elif 'Public' in item['univ_type']:
                    item['univ_type'] = 'Public'
                try:
                    item['intro_msg'] = univ.xpath('div[2]/div/div[2]/h4/text()').extract()[0]
                except IndexError:
                    item['intro_msg'] = univ.xpath('div[2]/h4/text()').extract()[0].strip()
                try:
                    item['description'] = univ.xpath('div[2]/div/div[2]/p/text()').extract()[0]
                except Exception:
                    item['description'] = ''
                try:
                    item['image_link'] = 'https://www.jpss.jp' +\
                        str(univ.xpath('div[2]/div/div[1]/a/img/@src').extract()[0])
                except Exception:
                    item['image_link'] = ''

            except Exception as e:
                print e
            logging.info(item)
            print item
            yield item
