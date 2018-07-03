import scrapy
import logging

logging.getLogger('scrapy').setLevel(logging.WARNING)

class BookWormSpider(scrapy.Spider):
    name = "BookWorm"
    start_urls = [ 
        # [pt] Inicialmente em uma categoria especifica, depois descobrir como entrar uma cateria pela entrada do usuario
        # [eng] As our first step we are starting with a specific category, in the near future the category will be determined by users 
        'https://www.ciadoslivros.com.br/livros-de-autoajuda'
    ]

    def parse(self, response):
    
        # [pt] extraindo informacoes de livros (nome,autor e preco)
        # [eng] extracting book informations (name, author and price)
        for book in response.xpath('//li[contains(@class,"product")]/div'):
            yield{
                'Title' : book.xpath('h3/a/@title').extract(), #.encode('utf-8')
                #'Author' : book.xpath('div[1]/a/text()').extract(),
                #'Price'  : book.xpath('div[@class = "info"]').extract(),

            }        
        pass

        # resquest de paginas

    pass

