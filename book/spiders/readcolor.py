import scrapy, sys
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
        sites = sel.xpath("//div[@class='span4']")
        items = []

        for site in sites:
            item = BookItem()
            item['name'] = site.xpath('a/div/div/h4/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            infos = site.xpath("a/div/div/ul[@class='unstyled']/li/text()").extract()
            for index, info in enumerate(infos):
                if(index == 0):
                    item['auther'] = info
                if(index == 1):
                    item['tag'] = info
            items.append(item)

        return items
