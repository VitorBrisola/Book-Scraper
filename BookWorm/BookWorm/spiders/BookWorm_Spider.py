import scrapy
import logging

logging.getLogger('scrapy').setLevel(logging.WARNING)

class BookWormSpider(scrapy.Spider):
    name = "BookWorm"
    start_urls = [
        'https://www.amazon.com.br/Livros/b/ref=nav__books_all?ie=UTF8&node=6740748011'
    ]

    def parse(self, response):
    
        # extrair informacoes de livros (nome,descricao e preco)

        # resquest de paginas

        pass