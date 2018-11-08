from datetime import datetime
from flask import request

# menu_items = []
delivery_orders = []

class Order:
    """Class to manipulate delivery order."""

    def __init__(self):
        # self.menu_items = menu_items
        self.delivery_orders = delivery_orders

    def get_all_orders(self):
        """Get list of all orders."""
        return self.delivery_orders

    def add_order(self, recipient, sender, parcel_details):
        """Create New order."""
        order = {
            "recipient":
            {"full_name":"ahmad", "phone_number": "256706196611", "select_country":"uganda", "destination":"kampala"
            },

            "sender":{
                "full_name":"shaqiri", "phone_number": "256706192255", "select_country":"kenya", "destination":"nairobi"
            },
            
            "parcel_details":{
                "weight_range": "1kg", "price":"500k", "created_at": str(datetime.now())
            }
        }
        self.delivery_orders.append(order)
        return order

    # def last_order_id(self):
    #     """Get last Id increment by 1."""
    #     if len(self.orders) < 1:
    #         return 1
    #     return self.orders[-1]['id'] + 1

    # def update_order_status(self, order_id, status):
    #     """Search order and update status if found."""
    #     order = self.search_order(order_id)
    #     if order:
    #         order[0].update({'status': status})
    #         return order
    #     return None

    # def update_order_details(self, order_id, location, quantity):
    #     """Search order and update details if found."""
    #     order = self.search_order(order_id)
    #     if order:
    #         order[0].update({'location': location, 'quantity': quantity})
    #         return order
    #     return None

    # def search_order(self, order_id):
    #     """Search specific order."""
    #     return [order for order in self.orders if order['id'] == int(order_id)]

    # def delete_order(self, order_id):
    #     """Remove this order from Order list."""
    #     search = self.search_order(order_id)
    #     if search:
    #         self.orders.remove(search[0])
    #         return True
    #     return False
