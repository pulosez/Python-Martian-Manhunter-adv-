from django.test import TestCase

from apps.cars.tests.factories import CarFactory
from apps.orders.models import Order


class TestOrderModel(TestCase):
    def setUp(self) -> None:
        self.car = CarFactory()

    def test_model(self):
        order = Order.objects.create(
            first_name='Olesia',
            last_name='Yaloveha',
            email='test_email@gmail.com',
            phone='+12025550195',
            message='some text message',
            car=self.car,
        )

        self.assertIsNotNone(order.id)
        self.assertEqual(str(order), 'Olesia Yaloveha')
        self.assertEqual(order.email, 'test_email@gmail.com')
        self.assertEqual(order.phone, '+12025550195')
        self.assertEqual(order.message, 'some text message')
