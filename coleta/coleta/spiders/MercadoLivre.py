import scrapy


class MercadoLivreSpider(scrapy.Spider):
    name = "MercadoLivre"
    allowed_domains = ["www.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/iphone-16"]

    def parse(self, response):
        pass
 