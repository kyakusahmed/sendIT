from flask import Flask, jsonify, request
from .manage import Order

app2 = Flask(__name__)
order = Order()

@app2.route('/api/v1/delivery_orders', methods=['POST'])
def add_one():
    data = request.get_json()
    if not data.get("recipient"):
        return jsonify({"error": "recipient is required"}), 200
    elif not data.get("sender"):
        return jsonify({"error": "sender is required"}), 200
    elif not data.get('parcel_details'):
        return jsonify({"error": "parcel_details required"}), 200
    return jsonify({"order": order.add_order(
                data["recipient"],
                data["sender"],
                data["parcel_details"]
            )}), 201

