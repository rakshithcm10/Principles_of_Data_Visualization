# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    author=scrapy.Field()
    tag=scrapy.Field()
    #pass


class CitiesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank=scrapy.Field()
    city=scrapy.Field()
    state=scrapy.Field()
    #pass


class AmazonItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()