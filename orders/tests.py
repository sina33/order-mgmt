from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Order

class OrderTests(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(username='admin', password='adminpass', is_staff=True)
        self.customer1 = User.objects.create_user(username='cust1', password='customer1pass')
        self.customer2 = User.objects.create_user(username='cust2', password='customer2pass')
        self.order1 = Order.objects.create(customer=self.customer1, product_name='Table', quantity=2, sum_price=100.00)
        self.order2 = Order.objects.create(customer=self.customer2, product_name='Chair', quantity=1, sum_price=30.00)

    def test_customer_can_only_see_their_orders(self):
        self.client.login(username='cust1', password='customer1pass')
        response = self.client.get('/api/orders/')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['product_name'], 'Table')

    def test_admin_can_see_all_orders(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get('/api/orders/')
        self.assertEqual(len(response.data), 2)

    def test_customer_cannot_edit_others_order(self):
        self.client.login(username='cust1', password='customer1pass')
        url = f'/api/orders/{self.order2.id}/'
        response = self.client.put(url, {'product_name': 'Bed', 'quantity': 1, 'sum_price': 120.00})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_admin_can_edit_any_order(self):
        self.client.login(username='admin', password='adminpass')
        url = f'/api/orders/{self.order2.id}/'
        response = self.client.put(url, {'product_name': 'Chair', 'quantity': 3, 'sum_price': 90.00})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customer_can_create_order(self):
        self.client.login(username='cust1', password='customer1pass')
        response = self.client.post('/api/orders/', {
            'product_name': 'Mug',
            'quantity': 1,
            'sum_price': 5.00
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.filter(customer=self.customer1).count(), 2)
