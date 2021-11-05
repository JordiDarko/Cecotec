from django.test import TestCase
from app1.models import Product
from django.contrib.auth.models import User
from app1.serializers import ProductSerializer
from rest_framework.test import RequestsClient, APITestCase
from rest_framework import status
from requests.auth import HTTPBasicAuth

# A continuación se muestran dos ejemplos de posibles tests, un TestCase de django y un APITestCase del rest framework.
# La aplicación no está completamente testeada pero ofrece la posiblidad de hacerlo.
class TestProductSerializer(TestCase):
    
    def test_expected_serilizer_json(self):
        expected_results = {
            'id' : 1,
            'name' : "deportivas",
            'price' : 35,
            'stock' : 60,
            'description' : "Perfectas para el deporte"
        }

        product = Product(**expected_results)
        results = ProductSerializer(product).data
        
        assert results == expected_results


class TestProductViews(APITestCase):

    def test_expected_response_data(self):
        url = 'http://localhost:8000/product_list/'
        
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        
        client = RequestsClient()
        client.auth = HTTPBasicAuth('testuser', '12345')
        
        response = self.client.get('/order/13/')
        response = client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
