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
        categorys = sel.xpath("//div[@class='tags']/a")
        del categorys[0]
        for category in categorys:
            url = category.xpath('@href')[0].extract()
            category_name = category.xpath('text()')[0].extract()
            yield scrapy.Request(url,
                                 callback=lambda response,
                                 category_name=category_name:
                                 self.parse_content(response, category_name))

    def parse_content(self, response, category_name):
        sel = Selector(response)
        sites = sel.xpath("//div[@class='span4']")

        for site in sites:
            item = BookItem()
            item['category'] = category_name
            item['name'] = site.xpath('a/div/div/h4/text()').extract()[0]
            item['url'] = site.xpath('a/@href').extract()[0]
            infos = site.xpath(
                "a/div/div/ul[@class='unstyled']/li/text()").extract()
            for index, info in enumerate(infos):
                if(index == 0):
                    item['auther'] = info
                if(index == 1):
                    item['tag'] = info
            yield item

        page = sel.xpath("//div[@class='pagination']")
        next_page = page.xpath("ul/li[@class='next']/a/@href")
        if next_page:
            url = next_page[0].extract()
            yield scrapy.Request(url,
                                 callback=lambda response,
                                 category_name=category_name:
                                 self.parse_content(response, category_name))
