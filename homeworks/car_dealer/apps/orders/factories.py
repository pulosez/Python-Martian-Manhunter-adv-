import factory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Order'

    first_name = 'Olesia'
    last_name = 'Yaloveha'
    email = 'test_email@test.com'
    phone = '+12025550195'
    car_id = 1
