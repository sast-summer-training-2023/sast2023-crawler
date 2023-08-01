# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import scrapy
import logging
import re

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
import selenium


class ZhihuSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class ZhihuDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        if not re.match(r"https://www.zhihu.com/question/\d+", request.url):
            return None

        chrome_opetions = ChromeOptions()
        chrome_opetions.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        # chrome_opetions.add_argument("--headless")
        driver = selenium.webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_opetions)
        driver.get(request.url)

        wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[2]/button')))

        button_quit = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/button')
        button_quit.click()

        while True:
            driver.execute_script("window.scrollBy(0, -10);")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            if driver.find_elements(By.XPATH, '//*[@id="root"]/div/main/div/div/div[3]/div[1]/div/div[2]/a/button'):
                break

        logging.info("finefine")
        
        response = scrapy.http.HtmlResponse(url=request.url, body=driver.page_source, encoding="utf-8", request=request)

        driver.quit()

        return response

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
