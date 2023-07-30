import scrapy


class HotpageSpider(scrapy.Spider):
    name = "hotpage"
    allowed_domains = ["zhihu.com"]
    start_urls = ["https://zhihu.com/hot"]

    def parse(self, response):
        pass
