# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#import sqlite3

#from itemadapter import ItemAdapter


class QuotetutorialPipeline:
    pass
    #def __init__(self):
        #self.create_connection()
        #self.create_table()
        
    #def create_connection(self):
     #   self.conn=sqlite3.connect("quotes.db")
      #  self.curr=self.conn.cursor() #cursor is used to perform transaction between python and database
        
    #def create_table(self):
     #   self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
      #  self.curr.execute("""create table quotes_tb(
       #     title text,
        #    author text,
         #   tag text
          #  )""")
        
   # def process_item(self, item, spider):
    #    self.store_db(item)
     #   return item
    
   # def store_db(self, item):
    #    self.curr.execute("""Insert into quotes_tb values(?,?,?)""",
     #                     (
      #                        item['title'][0],
       #                       item['author'][0],
        #                      item['tag'][0]
         #                     ))
       # self.conn.commit()
        
