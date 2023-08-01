# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    question_id = scrapy.Field()
    author_name = scrapy.Field()
    like_count = scrapy.Field()
