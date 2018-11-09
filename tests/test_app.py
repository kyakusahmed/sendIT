
import unittest
import json
from app.views import app2

class OrderTest(unittest.TestCase):
    
    def setUp(self):
        self.app = app2.test_client()
        self.app.testing = True
        self.parcel = { 
            "country": "uganda",
            "destination": "kampala",
            "parcel_price": "500k",
            "parcel_weight": "1kg",
            "pickup_location": "nairobi",
            "recepient_name": "Ahmad",
            "recepient_phone": "256706196611",
            "sender_id": 1,
            }
            

    def test_get_all_parcels(self):
        response = self.app.get("/api/v1/parcels")
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        self.assertIsInstance(data['parcels'], list)
    

    def test_get_parcel(self):
        self.app.post('/api/v1/parcels', json=self.parcel)
        response = self.app.get('/api/v1/parcel/1')
        assert response.status_code == 404

    def test_update_status(self):
        self.app.post('/api/v1/parcels', json=self.parcel)
        response =self.app.put('/api/v1/parcels/1', json={"status": "cancelled"})
        assert response.status_code == 200
   
    def test_parcel_not_found(self):
        response =self.app.get('/api/v1/parcel/12345')
        data = json.loads(response.get_data(as_text=True))
        assert data["message"] == "parcel not found"
        assert response.status_code == 404

    def test_update_status_sender_is_required(self):
        response = self.app.put('/api/v1/parcels/4676', json={"status": "completed"})
        data = json.loads(response.get_data(as_text=True))
        assert data["error"] == "sender is required"
        assert response.status_code == 200

    def test_get_all_parcels_by_user(self):
        response = self.app.get('/api/v1/parcels/sender/1')
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        self.assertIsInstance(data['parcels'], list)





