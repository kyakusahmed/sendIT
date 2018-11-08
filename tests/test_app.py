
import unittest
import json
from app.views import app2

class OrderTest(unittest.TestCase):
    
    def setUp(self):
        self.app = app2.test_client()
        self.app.testing = True
        self.delivery_orders = {"recipient":
            {"full_name":"ahmad", "phone_number": "256706196611", "select_country":"uganda", "destination":"kampala"
            },
            "sender":{
                "full_name":"shaqiri", "phone_number": "256706192255", "select_country":"kenya", "destination":"nairobi"
            },
            "parcel_details":{ 
            	"weight_range": "1kg", "price": "500k"
            },
            "status":"pending"}

    def test_get_all_orders(self):
        response = self.app.get("/api/v1/parcel_orders")
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        self.assertIsInstance(data['orders'], list)
    

    def test_get_order(self):
        self.app.post('/api/v1/delivery_orders', json=self.delivery_orders)
        response = self.app.get('/api/v1/delivery_orders/1')
        data = json.loads(response.get_data(as_text=True))
        assert data['order'][0]['id'] == 1
        assert data['order'][0]['recipient'] == {"full_name":"ahmad", "phone_number": "256706196611", "select_country":"uganda", "destination":"kampala"}
        assert data['order'][0]['sender'] == {"full_name":"shaqiri", "phone_number": "256706192255", "select_country":"kenya", "destination":"nairobi"}
        assert response.status_code == 200

    def test_update_status(self):
        self.app.post('/api/v1/parcel_orders', json=self.delivery_orders)
        response =self.app.put('/api/v1/parcel_orders/1', json={"status": "cancelled"})
        data = json.loads(response.get_data(as_text=True))
        assert data['order'][0]['status'] == "cancelled"
   
    def test_order_not_found(self):
        response =self.app.get('/api/v1/delivery_orders/12345')
        data = json.loads(response.get_data(as_text=True))
        assert data["message"] == "order not found"
        assert response.status_code == 404

    def test_update_status_not_found(self):
        response = self.app.put('/api/v1/parcel_orders/4676', json={"status": "completed"})
        data = json.loads(response.get_data(as_text=True))
        assert data["order"] == "Order not found"
        assert response.status_code == 200

