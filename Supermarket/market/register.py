#!/bin/python3

import pandas as pd
from inventoy import Stock

class CheckoutRegister(object):
    "A class for supermarket checkout"

    def __init__(self,inventory):
        '''initializing new object and properties.
        Should take no arguments'''

        self.inventory = Stock.create_connection(inventory)

    def scan_item(self,bar_code):
        ''' Check the inventory for the scanned bar_code
            and return the price if present'''

        self.price=self.inventory.query(bar_code)
        return self.price


    def accept_payment(self):
        '''Accept a list of products in bag and bill customer by adding the sub-totals'''

        # self.df.loc[self.df['prod_code']]
        pass


    def print_receipt(self):
        pass

if __name__ == '__main__':
    print('This is a module')
