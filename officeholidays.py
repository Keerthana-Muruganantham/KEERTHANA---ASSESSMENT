import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
class OfficeholidaysSpider(scrapy.Spider):
    name = 'officeholidays'
    allowed_domains = ['www.officeholidays.com/countries/india/2021']
    # start_urls = ['http://www.officeholidays.com/countries/india/2021/']
    def start_requests(self):
        yield scrapy.Request('http://www.officeholidays.com/countries/india/2021/', callback=self.parse)

    def parse(self, response):

        _list = []

        for ele in response.xpath('//table[@class="country-table"]/tbody/tr'):
            _dict = {}
            _dict['day'] = ele.xpath('td[1]/text()').get()
            _dict['date'] = ele.xpath('td/time/text()').get()
            _dict['holiday_name'] = ele.xpath('td/a/text()').get()
            _dict['type'] = ele.xpath('td[@class="comments"]/text()').get()
            _dict['comments'] = ele.xpath('td[@class="hide-ipadmobile"]/text()').get()
            _list.append(_dict)
        print(len(_list))
        df = pd.DataFrame(_list)
        # df.to_csv('holidays_list.csv', index=False, encoding='utf-8')
# CrawlerProcess()