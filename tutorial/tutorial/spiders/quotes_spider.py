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
            'http://quotes.toscrape.com/page/2/',
    ]
    
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Save file %s' % filename)
