import scrapy
import logging

logging.getLogger('scrapy').setLevel(logging.WARNING)

class MinerSpider(scrapy.Spider):
    name = "Miner"
    start_urls = [
        'https://www.searchtechnologies.com/blog/web-data-mining-tools-techniques',
    ]

    def parse(self, response):

        # Extracting page title
        yield{ 'title' : ''.join(response.css('div#block-st-zen-page-title>h1>span::text').extract())
                }

         # Extracting data
        #for quote in response.css('div.quote'):
            # making a dictionary with the data
        #    yield { 
        #        'text': quote.css('span.text::text').extract_first(),
        #        'author': quote.css('small.author::text').extract_first(),
        #        'tags': quote.css('div.tags a.tag::text').extract(),
        #    }

        pass
