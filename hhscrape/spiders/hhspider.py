import scrapy
from hhscrape.items import HhscrapeItem
from scrapy.http import Request
# To read from a csv file
import csv

class hhscrape(scrapy.Spider):
    name = 'hhspider'
    allowed_domains = ['hh.ru']
    start_url = 'https://hh.ru/vacancies/data-engineer?page=1&hhtmFrom=vacancy_search_catalog'

    request=Request(start_url)

    def parse(self, response):
        item = HhscrapeItem()
        content=response.xpath('(//h1)[1]')
        print(content)
