# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 12:36:11 2018

@author: vu
"""
import scrapy

class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    
    start_urls = ['http://quotes.toscrape.com/']
    
    def parse(self, response):
        # follow links to author pages
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)
            
        # follow pagination links
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)
            
    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
            
        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text')
        }
        
"""
By default, Scrapy filters out duplicated request URLs already visited.
This can be configured by the setting DUPEFILTER_CLASS
"""