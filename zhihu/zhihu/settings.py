# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "zhihu"

SPIDER_MODULES = ["zhihu.spiders"]
NEWSPIDER_MODULE = "zhihu.spiders"

LOG_LEVEL = "INFO"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "zhihu (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "*/*",
   "Accept-Language": "zh-CN,zh-Hans;q=0.9",
   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
   "Cookie": "KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1690882773|1690876150; tst=r; expire_in=15552000; z_c0=2|1:0|10:1690882764|4:z_c0|92:Mi4xd3RZREJBQUFBQUFBd0JkYkx4Y2tGeGNBQUFCZ0FsVk56Q0MyWlFCaDBNQ3F3LWlXZkNoWncyZnV3Tm1tQ1dkRGVB|94f0528913e52c8acde1e75377157609dc68d791c720c12b03a52a9b2f9ce015; o_act=login; ref_source=undefined; captcha_session_v2=2|1:0|10:1690882743|18:captcha_session_v2|88:N1BxUzFscVhTV0x1KzhCbm55ZmM5ODBPMjJ2VUFHNTNQNVV5ZDJQUnh2VE9NdjlnaG9ZWTQzRlJ2WnhOaEZzRg==|cb61033605e94a05977c904170a85b823559de20c58bd5697e0cbddcb25259ee; captcha_ticket_v2={validate:CN31_PJ65_nwxL9rFnYdTpZvw-xMNAmJosNsBAU5P1Tc5nLJ9QWlX.Jis6bsPTLYBohEII-NdYEsmVmX7RialRqx86uGydBh9SftY.sfqYk9NNXlfxbOMyZ-8hgvto6-gV9HT8iGr_HXBjsGzi2jY7Y9Rmxg1dRMD1FzWo8RvdpO1J59Ci4F95ZAMjeFfx0tuw7MaGYRLj9Q0KB-4kzlTlCn75LZn9IaVHnsb25wrw6ooImESLAFBRblv4OO10jP2Yj.8t5A9r4GS_0xRjL5ynehFjPB_FtmeSHZu25Go6aN2hhtdfIVQAxPKGwGyyZW8HkpiShTjwpLWhZ-9uacWdf4yIS406mpkeYlsCJbOzZQmlsCBcKvOIpdTjeG1FKAO1Tm4Mdxg7u.kmN7Sv5guTLsQaLfg1RoOMl_glZRxAmu0PVzrdPl6gAH7Me0jur-P4n7XowG1s.D4jO1B.dWzvn4aj-eQKNWZP_ptNASSTPBKkkywdUn4kxsfRhInsEz3}; YD00517437729195%3AWM_NI=Dvl%2FWOP9H1Og58OrxFPoG0qJxEIAVwl9SSfNoak81wGCPtsBm9Jf46FjFDE3EagbOIBhu0Vq1%2B5OgbNVqhsLb4Wf2XeHoRGh0TQSDGaoptQjMoalqbql%2FBiEf4TZ1D0ANzU%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea8d16eb594a695e24ab79e8fb2c14b879a9eadd874f7ec8ab0ed40969b8691ca2af0fea7c3b92a88aaa4d0d64594e788d2ce6df7e88193fb4e94b189d1f442bc9b87a2d57db0e79db4e546adbfa5d9b47d859da095f24aafe78687b73e86b68aa5c83987bfa983ce4382b8bbd1d57bf3f5fbb0e66a8e8abf89f248a2ec9987b154a798a1b3c664f48c9fb4c74da3b1c095d4628fb1af8df46ab3b4e1a3ec4fa6ec9cbbb450f49f829bd837e2a3; YD00517437729195%3AWM_TID=AbaaNomH2%2BpAAVAEEROUw4NGANmPLk2e; gdxidpyhxdE=i8jkT%5C3q3j3B5%2FRp%2BjLfbdVWzsr1k35pJ%2BO3Q8G2dz6%2F7GlxQlGtqDdDQ%2BrPoE%2FptMfY7l328rg2I1rC2TcPwATLqHW06%2FG7vwQS0ndXE0gStm%5CV3mK1WJvIiJYLayomZUrPWnyiRCZotU3pwgNQmMeDJhvSP5%2F2yOOEmyi8CMp5J%2FN2%3A1690883635762; JOID=UF4TAUKT_wSBMrylMpNwWOwMq44hzq1ivnPu6ECgvWfna-_lRX01w-U9uKE9AxTMuqZlnolDBuX0pYQyWDs96NU=; SESSIONID=YRb4JVMv8FcbRXDwUqBLvr8wwi2duDoLdG3MLJ2gdDx; osd=WlAQAU-Z8QeBP7arMZN9UuIPq4MrwK5is3ng60Ctt2nka-LvS341zu8zu6EwCRrPuqtvkIpDC-_6poQ_UjU-6Ng=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1690359604,1690608479,1690803806,1690864408; _xsrf=dYyDuH8HDe4IhqxZwsCe1pccLxPGWql8; q_c1=cdf6786e14a444d7a5a82ce85cd1dd71|1690359597000|1690359597000; _zap=63c0d0c0-8648-4aa7-b0f2-a1b1ec5c0ffc; d_c0=AMAXWy8XJBePTs5EUWNKDTpkpF6HuDfvsxk=|1690338988",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "zhihu.middlewares.ZhihuSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "zhihu.middlewares.ZhihuDownloaderMiddleware": 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "zhihu.pipelines.ZhihuPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
