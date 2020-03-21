# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import MapCompose, TakeFirst

def strip_processor(text):
    return text.strip()

class FrankSaltItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(strip_processor),
                        output_processor=TakeFirst())
    type = scrapy.Field(input_processor=MapCompose(strip_processor),
                        output_processor=TakeFirst())
    bedrooms = scrapy.Field(input_processor=MapCompose(strip_processor),
                            output_processor=TakeFirst())
    pool = scrapy.Field(input_processor=MapCompose(strip_processor),
                        output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(strip_processor),
                         output_processor=TakeFirst())
    locality = scrapy.Field(input_processor=MapCompose(strip_processor),
                            output_processor=TakeFirst())
    garden = scrapy.Field(input_processor=MapCompose(strip_processor),
                          output_processor=TakeFirst())
    finish = scrapy.Field(input_processor=MapCompose(strip_processor),
                          output_processor=TakeFirst())
    created_at = scrapy.Field(input_processor=MapCompose(strip_processor),
                              output_processor=TakeFirst())
    ref_id = scrapy.Field(input_processor=MapCompose(strip_processor),
                           output_processor=TakeFirst())
    views = scrapy.Field(input_processor=MapCompose(strip_processor),
                         output_processor=TakeFirst())
    url = scrapy.Field(input_processor=MapCompose(strip_processor),
                       output_processor=TakeFirst())



