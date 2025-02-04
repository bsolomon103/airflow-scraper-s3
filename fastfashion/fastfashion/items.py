# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FastfashionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    images = scrapy.Field()
    retailer = scrapy.Field()
    category = scrapy.Field()
    gender = scrapy.Field()
    brand = scrapy.Field()
    url = scrapy.Field()

