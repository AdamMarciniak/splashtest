import scrapy
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ["https://www.realcanadiansuperstore.ca/Food/Meat-%26-Seafood/c/RCSS001004000000"]

    
    

    
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, callback = self.parse, endpoint = 'render.html', args = {'wait':3},
                                headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                                                                                       ,'currentRegion' : 'CA-BC'})

    def parse(self, response):

        file = open('links2.txt' , 'w')

        item = {}
        item['urls'] = []
        
        itemList = response.css('div.product-name-wrapper > a.product-name::attr(href)').extract()

        for links in itemList:
            item['urls'].append(links)
            file.write(links)
            file.write('\n')

        

        yield item
        
        
        
        
        
