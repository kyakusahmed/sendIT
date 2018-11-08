from flask import Flask, jsonify, request
from .manage import Order

app2 = Flask(__name__)
order = Order()



@app2.route('/api/v1/delivery_orders/<int:id>', methods=['GET'])
def get_order(id):
    """get specific order."""
    parcel_order = order.search_order(id)
    if not parcel_order:
        return jsonify({"message": 'order not found'}), 404
    return jsonify({"order": parcel_order}), 200     

