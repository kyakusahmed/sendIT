from datetime import datetime
from flask import request

delivery_orders = []

class Order:
    """Class to manipulate delivery order."""

    def __init__(self):
        self.delivery_orders = delivery_orders

    def get_all_orders(self):
        """Get list of all orders."""
        return self.delivery_orders

    def add_order(self, recipient, sender, parcel_details):
        """Create New order."""
        order = {"id": len(self.delivery_orders) + 1, 
        "recipient":
        {"full_name":"ahmad", "phone_number": "256706196611", "select_country":"uganda", "destination":"kampala"
        },
        "sender":{
            "full_name":"shaqiri", "phone_number": "256706192255", "select_country":"kenya", "pickup_loc":"nairobi"
        },

        "parcel_details":{
            "weight_range": "1kg", "price":"500k", "created_at": str(datetime.now())
        },
        "status":"pending"
        }
        self.delivery_orders.append(order)
        return order

    def search_order(self, id):
        order = [order for order in self.delivery_orders if order['id'] == int(id)]
        if order:
            return order
        return None    

    def get_order(self, id):
        return self.search_order(id)

    def cancel_parcel_delivery_order(self, id, status):
        order = self.search_order(id)

        if order:
            order[0].update({"status": status})
            return order
        return "Order not found"        




   
   