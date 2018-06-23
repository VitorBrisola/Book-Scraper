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
        yield{ 
            'title' : response.css('title::text').extract_first(),
            #'urls' : ' '.join(response.css('p a::attr(href)').extract()), #gets all the urls in the page
            'NextPage' : response.css('p em a::attr(href)' or 'p a em::attr(href)').extract(), #gets the next page url
        }

        # preciso fazer com que liste a resquisicao de todas as urls extraidas
        # pois na segunda pagina ao extrair so a primeira url ele volta para a inicial 
        #next_page = response.css('em a::attr(href)').extract_first()
        #if next_page is not None:
        #    next_page = response.urljoin(next_page)
        #    yield scrapy.Request(next_page, callback=self.parse)

        # o html muda e nao consegue pegar o cap 4 pq a ordem de 'a em' para 'em a' ,tem que pegar os dois
        for a in (response.css('em a')):
            yield response.follow(a, callback=self.parse)
           

        #pass
