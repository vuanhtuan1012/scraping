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
        
        # response.follow supports relative URLs directly, no need to
        # call urljoin
        # response.follow returns a Request instance
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
            
        # We can also pass a selector to response.follow instead of a string
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback = self.parse)
            
        # for <a> elements, response.follow uses their href attribute
        # automatically
        for a in response.css('li.next a'):
            yield response.follow(a, callback = self.parse)