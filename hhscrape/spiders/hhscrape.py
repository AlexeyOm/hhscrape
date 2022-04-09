import scrapy
from hhscrape.items import HhscrapeItem
from scrapy.http import JsonRequest
# To read from a csv file
import csv
import json

class hhscrape(scrapy.Spider):
    name = 'hhscrape'
    allowed_domains = ['hh.ru']
    start_urls = ['https://api.hh.ru/vacancies?text=data-enginner&period=2&per_page=30&page=0']

    request = JsonRequest(start_urls[0])


    def parse(self, response):
        item = HhscrapeItem()
        hh_json = json.loads(response.body.decode(response.encoding))
        print("-------------------")
        for vacancy in hh_json['items']:
            print(vacancy['id'])
            print(vacancy['name'])
            print(vacancy['area']['name'])
            if vacancy['salary']:
                salary_min = vacancy['salary']['from']
                salary_max = vacancy['salary']['to']
                salary_currency = vacancy['salary']['currency']
                salary_gross = vacancy['salary']['gross']
                salary_is_hidden = False
            else:
                salary_is_hidden = True
        if hh_json['pages'] > hh_json['page'] + 1:
            print("goind to the next page" + str(hh_json['page'] + 1))
            request = JsonRequest(start_urls[0].replace("page=0","page=" + str(hh_json['page'] + 1) ))
            pass
        print("-------------------")
        
            

        
