from datetime import datetime
from flask import request

delivery_orders = []

class Order:
    """Class to manipulate delivery order."""

    def __init__(self):
        self.delivery_orders = delivery_orders

   
    def search_order(self, id):
        order = [order for order in self.delivery_orders if order['id'] == int(id)]
        if order:
            return order
        return None    

    




   
   