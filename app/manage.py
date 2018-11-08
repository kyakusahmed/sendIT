from datetime import datetime
from flask import request

delivery_orders = []

class Order:

    def __init__(self):
        self.delivery_orders = delivery_orders

    def search_order(self, id):
        order = [order for order in self.delivery_orders if order['id'] == int(id)]
        if order:
            return order
        return None 

    def cancel_parcel_delivery_order(self, id, status):
        order = self.search_order(id)
        if order:
            order[0].update({"status": status})
            return order
        return "Order not found"        




   
   