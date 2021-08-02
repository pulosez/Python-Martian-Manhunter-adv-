import factory


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.Country'

    name = 'Germany'


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.City'

    name = 'Berlin'
    country_id = 2
