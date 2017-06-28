from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from cl_1024.items import Cl1024Item
import scrapy.http


class ClCommunitySpider(CrawlSpider):
    name = 'cl_spider'

    download_delay = 1

    allowed_domains = []

    def start_requests(self):
        pages = []
        for i in range(1, 100):
            url = 'http://t66y.com/thread0806.php?fid=22&search=&page=%s'
            page = scrapy.Request(url)
            pages.append(page)
        return pages

    def parse(self, response):
        print response

        sel = Selector(response)
        item = Cl1024Item()

        movie_name = sel.xpath("//h3/a/text()").extract()
        url = sel.xpath("//h3/a/@href").extract()

        print '------------'
        print movie_name
        print '------------'

        item['movie_name'] = [n.encode('utf-8') for n in movie_name]
        item['url'] = [n.encode('utf-8') for n in url]

        yield item
