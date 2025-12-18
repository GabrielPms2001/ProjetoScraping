import scrapy


class MercadoLivreSpider(scrapy.Spider):
    name = "MercadoLivre"
    allowed_domains = ["www.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/iphone-16"]
    page_count = 1
    max_pages = 10

    def parse(self, response):
        products = response.css('div.ui-search-result__wrapper')
        
        for product in products:

            prices = product.css('span.andes-money-amount__fraction::text').getall()


            yield {
                'brand': product.css('span.poly-component__seller::text').get(),
                'name': product.css('a.poly-component__title::text').get(),
                'old_price': prices[0] if len(prices) > 0 else None,
                'new_price': prices[1] if len(prices) > 0 else None,
                'reviews': product.css('span.andes-visually-hidden::text').get()
            }
        
        if self.page_count < self.max_pages:
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next::attr(href)').get()
            if next_page:
                self.page_count += 1
        yield scrapy.Request(url=next_page, callback=self.parse)