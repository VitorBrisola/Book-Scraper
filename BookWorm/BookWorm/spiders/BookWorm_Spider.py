import scrapy
import logging

logging.getLogger('scrapy').setLevel(logging.WARNING)

class BookWormSpider(scrapy.Spider):
    name = "BookWorm"
    start_urls = [
        'https://www.amazon.com.br/Livros/b/ref=nav__books_all?ie=UTF8&node=6740748011'
    ]

    def parse(self, response):
    
        # [pt] extraindo informacoes de livros (nome,descricao e preco)
        # [eng] extracting book informations (name, description and price)
        yield{
            # [pt] tentando extrair o titulo de qualquer link de livro da amazon por Xpath - NAO ESTA FUNCINANDO AINDA
            # [eng] trying to extract book titles from amazon with xpath - ITS NOT WORKING YET
            'Title' : response.xpath("//li[@class = 'acswidget-carousel-redesign__card']/span").extract_first()
        }        

        # resquest de paginas

        pass
