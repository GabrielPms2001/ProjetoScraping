import scrapy


class MercadoLivreSpider(scrapy.Spider):
    name = "MercadoLivre"
    allowed_domains = ["www.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/iphone-16"]

    def parse(self, response):
        products = response.css('div.ui-search-result__wrapper')
        
        for product in products:
            yield {
                'brand': product.css('span.poly-component__seller::text').get(),
                'name': product.css('a.poly-component__title::text').get()
                #'old_price':
                #'new_price':
                #'reviews_rating_number':
                #'reviews_amount':

            }