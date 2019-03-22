#!/bin/python3

import os
import sqlite3
from sqlite3 import Error

class Stock(object):
    '''the database for the supermarket inventory '''

    def __init__(self):
        'initialize '
        # self.db_file = db_file
        self.sql_create_inventory_table = ""
        self.rows = 0
        self.sql  =""
        self.item = ()

    def create_connection(self,db_file):
        '''Create connection or create database if abscent '''
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        else: #incase no error is encountered
            self.cur = self.conn.cursor()
            self.__create_table()

    def insert(self,item):
        '''Will insert items into the database.
        This goes for new items for the stock.Accepts a tuple as an argument'''

        self.sql = '''INSERT INTO inventory(name,quantity,price) VALUES (?,?,?) '''
        self.cur.execute(self.sql,item)

    def __create_table(self):
        '''Create table for those running program for first time '''

        self.sql_create_inventory_table = """CREATE TABLE IF NOT EXISTS inventory(
        id integer PRIMARY KEY,
        bar_code integer NOT NULL,
        name text NOT NULL,
        quantity integer NOT NULL,
        price integer NOT NULL
        );

         """

        try:
            self.cur.execute(self.sql_create_inventory_table)
        except Error as e:
            print(e)

    def update(self,name,quantity,price=None):
        '''Incase an item is taken from the inventory,update the item as taken
        Price argument is optional '''

        self.item = (quantity,price,name)
        self.sql = '''UPDATE inventory SET quantity=?,
                                    price=?
                                    WHERE name=? '''
        self.cur.execute(self.sql,self.item)
        pass

    def query(self,bar_code):
        '''Look for the specified item in the inventory and return the price'''

        self.cur.execute('SELECT price FROM tasks WHERE bar_code=? ',(bar_code,))
        self.rows = cur.fetchall()

        for row in self.rows:
            return row

    def delete(self,name):
        '''Remove item from inventory incase not being sold any more'''

        self.sql = 'DELETE FROM inventory WHERE name=?'
        self.cur.execute(self.sql,(name,))



if __name__ =='__main__':
    print("This program is intended for use as a module ")
