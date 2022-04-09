# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class HhscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    salary = Field()
    employer = Field()
    rating = Field()
    city = Field()
    people_watching = Field()
    full_text = Field()
    required_experience = Field()
    employment_mode = Field()
    key_skills = Field()
