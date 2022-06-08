# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmznItem(scrapy.Item):
    username= scrapy.Field()
    type= scrapy.Field()
    reviewTitles= scrapy.Field()
    reviewBody= scrapy.Field()
    verifiedPurchase= scrapy.Field()
    postDate= scrapy.Field()
    starRating= scrapy.Field()
    helpful = scrapy.Field()
    type_product = scrapy.Field()
    special_profile = scrapy.Field()

    
