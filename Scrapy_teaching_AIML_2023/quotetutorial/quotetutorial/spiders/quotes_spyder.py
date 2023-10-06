# -*- coding: utf-8 -*-

import scrapy
from ..items import QuotetutorialItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    page_number=2
    start_urls = (
        'http://quotes.toscrape.com/page/1/',
    )

    def parse(self, response):
        items=QuotetutorialItem()
        
        all_div_quotes=response.css('div.quote')
        
        
        for quotes in all_div_quotes:
            
            title=quotes.css('span.text::text').extract()
            author=quotes.css('.author::text').extract()
            tag=quotes.css('.tag::text').extract()
            
            items['title']=title
            items['author']=author
            items['tag']=tag
            
            
            yield items
            
        next_page = 'http://quotes.toscrape.com/page/'+str(QuotesSpider.page_number)+'/'
       
        if QuotesSpider.page_number < 11:
            yield response.follow(next_page, callback = self.parse)
            QuotesSpider.page_number += 1