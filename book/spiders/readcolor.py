import scrapy
from scrapy.selector import Selector
from book.items import BookItem


class Readcolor(scrapy.spiders.Spider):
    name = "readcolor"
    allowed_domains = ["readcolor.com"]
    start_urls = [
        "http://readcolor.com/books"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath("//div[@class='span7']")
        items = []

        for site in sites:
            item = BookItem()
            item['name'] = site.xpath('h4/text()').extract()
            items.append(item)

        return items
