# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
import sqlite3


class AssignmentPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
        
    def create_connection(self):
        self.conn=sqlite3.connect("assignment_3.db")
        self.curr=self.conn.cursor()
        
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS assignment_3_tb""")
        self.curr.execute("""create table assignment_3_tb(
            name text,
            price text
            )""")
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
         self.curr.execute("""Insert into assignment_3_tb values(?,?)""",
                           (
                               item['name'],
                               item['price']
                              ))
         self.conn.commit()
    