# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com/']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        Hello = 'Hello'
        Pirnt Hello
