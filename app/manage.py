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

    