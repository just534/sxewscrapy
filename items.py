# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    money=scrapy.Field()
    price=scrapy.Field()
    detail=scrapy.Field()
    area=scrapy.Field()
    towards=scrapy.Field()
    pass
