# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LegoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    shop_avatar = scrapy.Field()
    shop_name = scrapy.Field()
    product_link = scrapy.Field()
    product_title = scrapy.Field()
    product_img = scrapy.Field()
    product_price = scrapy.Field()
    product_slaes_month = scrapy.Field()
    product_slaes_count = scrapy.Field()
    product_stock = scrapy.Field()
    collection = scrapy.Field()
    product_id = scrapy.Field()
    pass
