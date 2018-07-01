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
    
        # [pt] extraindo informacoes de livros (nome,descricao e preco)
        # [eng] extracting book informations (name, description and price)

        for title in (response.xpath('//h3/a/@title').extract()):
            yield{
                'Title' : title.encode('utf-8')
            }        
        pass

        # resquest de paginas

        pass

# ainda nao consegui resolve-los, talvez seja melhor tentar com outro site
# ultimos xpath teste
#li[@class = "a-carousel-card acswidget-carousel__card"]
#h2[@class = 'a-spacing-mini acswidget-carousel__header']