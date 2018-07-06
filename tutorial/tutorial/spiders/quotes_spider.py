# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 10:25:42 2018

@author: vu
"""

import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    
    start_urls = [
            'http://quotes.toscrape.com/page/1/',
    ]
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract()
            }
        
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback = self.parse)
