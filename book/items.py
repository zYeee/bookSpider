# -*- coding: utf-8 -*-
from scrapy import Item, Field


class BookItem(Item):
    # define the fields for your item here like:
    name = Field()
    auther = Field()
    tag = Field()
    url = Field()
    category = Field()
