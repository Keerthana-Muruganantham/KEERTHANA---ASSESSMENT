import pandas as pd
import scrapy
import json
class MeeshoMensSpider(scrapy.Spider):
    name = 'meesho_mens'
    allowed_domains = ['meesho.com']
    start_urls = ['http://meesho.com/']

    def parse(self, response):
        men_text = response.text.split('{"id":4,"title":"Men"')[1].split(',{"id":5,"title":"Beauty')[0]
        men_text = '{"id":4,"title":"Men"' + men_text
        data = json.loads(men_text)
        _list = []
        for cat in data['level_2']:
            for sub_cat in cat['level_3']:
                _dict = {}
                _dict['category'] = cat['title']
                _dict['sub_category'] = sub_cat['title']
                _list.append(_dict)
        df = pd.DataFrame(_list)
        df.to_csv('meesho_mens_category.csv', index=False, encoding='utf-8')
