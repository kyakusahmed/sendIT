from flask import Flask, jsonify, request
from .manage import Order

app2 = Flask(__name__)
order = Order()

@app2.route('/api/v1/parcel_orders', methods=['GET'])
def get_all_orders():
    return jsonify({'orders': order.get_all_orders()}), 200

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

@app2.route('/api/v1/delivery_orders/<int:id>', methods=['GET'])
def get_order(id):
    """get specific order."""
    parcel_order = order.search_order(id)
    if not parcel_order:
        return jsonify({"message": 'order not found'}), 404
    return jsonify({"order": parcel_order}), 200     

@app2.route('/api/v1/parcel_orders/<int:id>', methods=['PUT'])
def update_status(id):
    get_input = request.get_json()
    if not get_input.get("status"):
        return jsonify({"error" : "status is required"}), 200
    return jsonify({"order" : order.cancel_parcel_delivery_order(id, get_input["status"])}), 200
    

# @app2.route('/api/v1/parcel_orders/<int:user_id>', methods=['GET'])
# def 