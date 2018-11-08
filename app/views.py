from flask import Flask, jsonify, request
from .manage import Order

app2 = Flask(__name__)
order = Order()

@app2.route('/api/v1/orders/<int:id>', methods=['PUT'])
def cancel_parcel_delivery_order(id):
    get_input = request.get_json()
    if not get_input.get("status"):
        return jsonify({"error" : "status is required"}), 200
    return jsonify({"order" : order.cancel_parcel_delivery_order(id, get_input["status"])}), 200
