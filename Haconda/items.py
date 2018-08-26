# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HacondaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    source = scrapy.Field()
    univ_type = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    intro_msg = scrapy.Field()
    image_link = scrapy.Field()
    information_link = scrapy.Field()
    location = scrapy.Field()
    undergraduate = scrapy.Field()
    link = scrapy.Field()
