import newspaper

from BeautifulSoup import BeautifulSoup
from scrapy.spider import BaseSpider
from multiprocessing import Process, Queue
from scrapy.http import Request



class GuardianSpider(BaseSpider):
    # name has to be same as the project that you started
    name = "mayhem"
    allowed_domains = ["theguardian.com"]

    def __init__(self, *args, **kwargs):
        super(GuardianSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["http://www.theguardian.com/international"]

    def parse_node(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
        soup = BeautifulSoup("".join(response.body))
        cells = soup.findAll('a', {"class" : "global-navigation__action"})
        for cell in cells:
            print cell["href"]
            # this is the parsed url for each class of articles
            # extend the project base on this one!!!!

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return Request(url, dont_filter=True)

    def __doc__():
        # add some docs for each spider class
        pass
