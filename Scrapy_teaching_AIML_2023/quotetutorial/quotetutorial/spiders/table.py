# -*- coding: utf-8 -*-

import scrapy
from ..items import CitiesItem

class CitiesSpider(scrapy.Spider):
    name = "cities"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = (
        'https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population',
    )
    
    def parse(self, response):
        cities=CitiesItem()
        table = response.xpath('//table[contains(@class, "wikitable")]')[0]
        trs = table.xpath('.//tr')
        rank = trs.xpath('.//td[1]/text()').extract()
        city = trs.xpath('.//td[2]//text()').extract()
        state = trs.xpath('.//td[5]//text()').extract()

        cities['rank']=rank
        cities['city']=city
        cities['state']=state
            
        yield cities