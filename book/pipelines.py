import MySQLdb
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BookPipeline(object):
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "123456", "book")
        self.db.set_character_set('utf8')

    def process_item(self, item, spider):
        cursor = self.db.cursor()
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
        sql = "INSERT INTO readcolor (name, category, auther, tag, url)\
            VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, [item['name'], item['category'],
                             item['auther'], item['tag'], item['url']])
        self.db.commit()
        cursor.close()
        return item

    def spider_closed(self, spider):
        self.db.close()
