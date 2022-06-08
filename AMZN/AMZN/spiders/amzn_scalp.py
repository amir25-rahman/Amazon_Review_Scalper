import scrapy
from AMZN.items import AmznItem
#cd C:\Users\Null\Desktop\python_tur\AMZN\AMZN\spiders
#scrapy runspider amzn_scalp.py
#scrapy runspider amzn_scalp.py -o data.csv -t csv

import os
if os.path.exists("data.csv"):
  os.remove("data.csv")
else:
  print("The file does not exist") 

class AmznScalpSpider(scrapy.Spider):
    name = 'amzn_scalp'
    page_number = 2
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Echo-Dot/product-reviews/B07XJ8C8F5/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews']
    next_url = str(start_urls).split('=cm_cr_dp_d_show_all_btm')[0] + '=cm_cr_dp_d_show_all_btm_next_'
    next_page = next_url + str(page_number) + '?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(page_number)

    def parse(self, response):
        items = AmznItem()
        products = response.xpath("//div[@class='a-section review aok-relative']")
        for item in products:
          
          items['username'] = item.xpath('.//span[@class="a-profile-name"]/text()').get() 
          items['helpful'] = item.xpath('.//span[@data-hook="helpful-vote-statement"]/text()').get()
          items['starRating'] = item.xpath('.//i[@data-hook="review-star-rating"]/span/text()').get()
          items['type'] = item.xpath('.//a[@data-hook="format-strip"]/text()').get()
          items['type_product'] = item.xpath('.//i[@class="a-icon a-icon-text-separator"]/following-sibling::text()').get()
          items['postDate'] = item.xpath('.//span[@data-hook ="review-date"]/text()').get()
          items['verifiedPurchase'] = item.xpath('//span[@data-hook="avp-badge"]/text()').get()
          items['reviewBody'] = item.xpath('string(.//span[@data-hook="review-body"]/span)').get()
          items['reviewTitles'] = item.xpath('.//a[@data-hook="review-title"]/span/text()').get()
          items['special_profile'] = item.xpath('.//span[@class="a-profile-descriptor"]/text()').get()

          yield items

#         #You want how many pages????? 5 = 40 rows (10 per page - 1st page)
#         ****************************************
#         if AmznScalpSpider.page_number < 4:
          
#           AmznScalpSpider.page_number += 1
#           print('Page Number Is: ', AmznScalpSpider.page_number)
#           yield response.follow(AmznScalpSpider.next_page, callback = self.parse)
# ****************************************
#           #yield scrapy.Request(url=AmznScalpSpider.next_page, callback= self.parse)

        
        next_page = 'https://www.amazon.com/Echo-Dot/product-reviews/B07XJ8C8F5/ref=cm_cr_arp_d_paging_btm_next_' + str(AmznScalpSpider.page_number) + '?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(AmznScalpSpider.page_number)
        if AmznScalpSpider.page_number < 100:
          AmznScalpSpider.page_number += 1
          yield response.follow(next_page, callback = self.parse)
        

    
     


