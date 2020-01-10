# -*- coding: utf-8 -*-
import scrapy
from ..items import SpiderDetailItem

class SxewSpider(scrapy.Spider):
    name = 'sxew'
    allowed_domains = ['e0575.com']
    base_url = 'https://house.e0575.com/list.php?tix=1&page={}'
    start_urls=[]
    for i in range(1,4):
        start_urls.append(base_url.format(i))
    print(start_urls)

    def parse(self, response):
        content_lis=response.xpath('//div[@class="main1 main3"]/div[@class="l"]/ul[@class="fy_list1"]/li')
        for li in content_lis:
            url=li.xpath('./div[@class="con1"]/h1/a/@href').extract_first()
            url='https://house.e0575.com/'+url
            yield scrapy.Request(url,callback=self.detailparse)

    def detailparse(self,response):
        item=SpiderDetailItem()
        item['title']=response.xpath('//div[@class="show1_t1"]/text()').extract_first()
        item['money']=response.xpath('//div[@class="show1_t1"]/div[@class="show1_t1m"]/text()').extract_first()
        item['price']=response.xpath('//div[@class="show1_t1"]/div[@class="show1_t1m"]/em/text()').extract_first()
        item['area']=response.xpath('//div[@class="show1_d1"]/div[@class="show1_d1_l"]/ul[@class="cs1"]/li[7]').extract_first()
        item['towards']=response.xpath('//div[@class="show1_d1"]/div[@class="show1_d1_l"]/ul[@class="cs1"]/li[5]').extract_first()

        print(item)