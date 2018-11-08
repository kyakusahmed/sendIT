from flask import Flask, jsonify, request
from .manage import Order

app2 = Flask(__name__)
order = Order()

@app2.route('/api/v1/parcel_orders', methods=['GET'])
def get_all_orders():
    """Get all orders"""
    return jsonify({'orders': order.get_all_orders()}), 200

