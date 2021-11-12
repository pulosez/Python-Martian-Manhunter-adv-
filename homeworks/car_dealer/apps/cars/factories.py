import factory


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Car'

    number = 'AA 4567 AA'
    slug = '120-MT'
    engine_power = 120
    dealer_id = 1
    picture_id = 1
    color_id = 1
    model_id = 1


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Color'

    name = 'Red'


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Brand'

    name = 'Audi'


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Property'

    name = 'Coupe'


class PictureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Picture'

    position = 3
    metadata = 'Third metadata'
    url = factory.django.ImageField(from_path='pictures/test.jpg')


class ModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Model'

    name = 'A5'
    brand_id = 2
