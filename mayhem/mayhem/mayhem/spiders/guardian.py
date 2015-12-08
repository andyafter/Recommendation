from scrapy.spider import BaseSpider


class GuardianSpider(BaseSpider):
    name = "guardian"
    allowed_domains = ["theguardian.com"]
    start_urls = [
        "http://www.theguardian.com/international"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)

    def __doc__():
        # add some docs for each spider class
        pass
