import scrapy


class HihappySpider(scrapy.Spider):
    name = "HiHappy"
    allowed_domains = ["www.rihappy.com.br"]
    start_urls = ["https://www.rihappy.com.br/brinquedos/quebra-cabecas/quebra-cabecas-3d"]

    def parse(self, response):
        pass
