import scrapy


class PhoneSpider(scrapy.Spider):
    name = "phone"
    allowed_domains = ["api.digikala.com"]
    start_urls = ["https://api.digikala.com/v1/categories/mobile-phone/search/?attributes%5B2251%5D%5B0%5D=19476&brands%5B0%5D=18&brands%5B1%5D=1662&q=%DA%AF%D9%88%D8%B4%DB%8C&sort=20&page=1"]

    def parse(self, response):
        pass
