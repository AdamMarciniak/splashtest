import scrapy
from scrapy_splash import SplashRequest
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ["https://www.realcanadiansuperstore.ca/Food/Fruits-%26-Vegetables/c/RCSS001001000000"]
    WAIT_TIME = 10


    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, callback = self.parse, endpoint = 'render.html', args = {'wait':self.WAIT_TIME,'images':0},)


    def parse(self, response):

        seeAllList1 = []

        sel1 = response.selector.css('li[data-level="1"]')[1:10]

        sel2 = sel1.css('li[data-level="3"] > a.sub-nav-link::attr(href)')

        seeAllList1 = sel2.extract()
        print("------------MAIN LINKS------------------\n")
        print(seeAllList1)
        print('\n\n')

        yield None
