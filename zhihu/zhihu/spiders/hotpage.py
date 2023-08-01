import scrapy
from scrapy.http import Request
import logging
import re


class HotpageSpider(scrapy.Spider):
    name = "hotpage"
    allowed_domains = ["zhihu.com"]
    start_urls = ["https://zhihu.com/hot"]

    def parse(self, response):
        logging.info(response.url)
        for item in response.xpath("//div[@class='HotItem-content']"):
            yield Request(
                url=item.xpath("./a/@href").extract_first(), callback=self.parse_detail
            )
            break

    def parse_detail(self, response):
        logging.info(response.url)
        question_id = re.findall(r"question/(\d+)", response.url)[0]
        items = response.xpath(
            '//*[@id="QuestionAnswers-answers"]//*[@class="List-item"]'
        )
        logging.info(f"question_id: {question_id}, items: {len(items)}")
        for item in items:
            author_name = item.xpath(
                './/div[@class="AuthorInfo"]//meta[@itemprop="name"]/@content'
            ).extract_first()
            try:
                like_num = item.xpath(
                    './/div[@class="ContentItem-actions RichContent-actions"]/span[1]/button[1]/@aria-label'
                ).extract_first()[3:-1]
            except Exception:
                like_num = item.xpath(
                    './/div[@class="ContentItem-actions"]/span[1]/button[1]/@aria-label'
                ).extract_first()[3:-1]
            yield {
                "question_id": question_id,
                "author_name": author_name,
                "like_num": like_num,
            }
