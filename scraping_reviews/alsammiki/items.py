# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Review(scrapy.Item):
    product_name = scrapy.Field()
    subject = scrapy.Field()
    text = scrapy.Field()
    date = scrapy.Field()
