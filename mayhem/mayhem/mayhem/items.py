# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class NewsSection(scrapy.Item):
    # This will be used later to define the object structure for
    # all the news articles.
    section = Field()
    link = Field()


class NewsArticle(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    link = Field()
    description = Field()
