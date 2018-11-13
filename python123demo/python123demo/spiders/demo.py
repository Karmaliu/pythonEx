# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['python123.io']
    start_urls = ['http://www.runoob.com/python3/python3-string-len.html']
    
    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname,'w') as f:
            f.write(response.body)
        self.log('Save file %s' % fname)

