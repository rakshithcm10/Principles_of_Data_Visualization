import scrapy
from ..items import AssignmentItem

class AssignmentSpider(scrapy.Spider):
    name='assignment_3'
    allowed_domain=['j2store.net']
    start_urls=['https://j2store.net/demo/index.php/shop']
    page_number = 1
    
    def parse(self,response):
        items=AssignmentItem()
        products=response.css("div.col-sm-9 div[itemprop=itemListElement]")
        for product in products:
            name=product.css("h2.product-title a::text").get().strip()
            price=product.css("div.sale-price::text").get().strip()
            
            items['name']=name
            items['price']=price
            
            yield items
                
        
        next_page = f'https://j2store.net/demo/index.php/shop?start={self.page_number * 9}'
        if self.page_number < 5:
            self.page_number += 1
            yield response.follow(next_page, callback=self.parse)