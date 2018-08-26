# -*- coding: utf-8 -*-

import scrapy
import time
import csv
import logging
from Haconda.items import HacondaItem

class JapanUnivInformationSpider(scrapy.Spider):
    name = "info_jp_jpss"
    start_urls = [
            "https://www.jpss.jp/en/search/?tb=1&a%5Bnm%5D=&a%5Bfw%5D=&u%5Bfc%5D=&u%5Bdp%5D=%E6%83%85%E5%A0%B1&u%5Bac%5D=&a%5Bpf%5D=8-9-10-11-12-13-14-15-19-20&search=search",
            "https://www.jpss.jp/en/search/?p=2&tb=1&a%5Bnm%5D=&a%5Bfw%5D=&a%5Bpf%5D=8-9-10-11-12-13-14-15-19-20&u%5Bac%5D=&u%5Bfc%5D=&u%5Bdp%5D=%E6%83%85%E5%A0%B1&g%5Brs%5D=&g%5Bmj%5D=&search=search",
            "https://www.jpss.jp/en/search/?p=3&tb=1&a%5Bnm%5D=&a%5Bfw%5D=&a%5Bpf%5D=8-9-10-11-12-13-14-15-19-20&u%5Bac%5D=&u%5Bfc%5D=&u%5Bdp%5D=%E6%83%85%E5%A0%B1&g%5Brs%5D=&g%5Bmj%5D=&search=search",
            "https://www.jpss.jp/en/search/?p=4&tb=1&a%5Bnm%5D=&a%5Bfw%5D=&a%5Bpf%5D=8-9-10-11-12-13-14-15-19-20&u%5Bac%5D=&u%5Bfc%5D=&u%5Bdp%5D=%E6%83%85%E5%A0%B1&g%5Brs%5D=&g%5Bmj%5D=&search=search",
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

                item['name'] = ' | '.join(univ.xpath('div[1]/div[1]/h3/a/span/text()').extract())
                try:
                    item['intro_msg'] = univ.xpath('div[2]/div/div[2]/h4/text()').extract()[0]
                except IndexError:
                    item['intro_msg'] = univ.xpath('div[2]/h4/text()').extract()[0].strip()
                try:
                    item['description'] = univ.xpath('div[2]/div/div[2]/p/text()').extract()[0]
                except Exception:
                    item['description'] = ''
                item['link'] = 'https://www.jpss.jp' +\
                        str(univ.xpath('div[1]/div[1]/h3/a/@href').extract()[0])
                try:
                    item['image_link'] = 'https://www.jpss.jp' +\
                            str(univ.xpath('div[2]/div/div[1]/a/img/@src').extract()[0])
                except Exception:
                    item['image_link'] = ''
                item['undergraduate'] = univ.xpath('div[2]/ul/li/a/@title').extract()

            except Exception as e:
                print e
            print item
            yield item
