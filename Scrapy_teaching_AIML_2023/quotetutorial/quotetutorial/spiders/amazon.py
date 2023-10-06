import scrapy
from ..items import AmazonItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.in/s?k=fan&ref=nb_sb_noss_2']

    def parse(self, response):
        product_blocks = response.css('.s-result-item')
        
        for product_block in product_blocks:
            item = AmazonItem()
            
            item['name'] = product_block.css('.a-size-medium.a-color-base.a-text-normal::text').get()
            item['price'] = product_block.css('.a-price .a-offscreen::text').get()
            item['rating'] = product_block.css('.a-size-base.puis-normal-weight-text::text').extract()

            # Clean the data
            item['name'] = item['name'].strip() if item['name'] else None
            item['price'] = item['price'].strip() if item['price'] else None

            yield item
