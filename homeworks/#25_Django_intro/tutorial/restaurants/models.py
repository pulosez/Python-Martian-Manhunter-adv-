from django.db import models


class Restaurant(models.Model):
    title = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(
        'restaurants.City',
        on_delete=models.CASCADE,
    )
    employers = models.ManyToManyField(
        'restaurants.Employee',
    )
    menus = models.ManyToManyField(
        'restaurants.Menu',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'


class Employee(models.Model):
    JOB_CHEF = 'chef'
    JOB_MANAGER = 'manager'
    JOB_WAITER = 'waiter'
    JOB_CLEANER = 'cleaner'

    JOB_CHOICES = (
        (JOB_CHEF, "Restaurant Head Chef"),
        (JOB_MANAGER, "Restaurant Manager"),
        (JOB_WAITER, "Restaurant Waiter/Waitress"),
        (JOB_CLEANER, "Restaurant Cleaner"),
    )

    name = models.CharField(max_length=80, null=False)
    phone = models.CharField(max_length=50)
    job = models.CharField(
        max_length=30,
        choices=JOB_CHOICES,
        default=JOB_WAITER,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employers'


class Country(models.Model):
    title = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class City(models.Model):
    title = models.CharField(max_length=100, null=False)
    country = models.ForeignKey(
        'restaurants.Country',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Dish(models.Model):
    title = models.CharField(max_length=150, null=False)
    width = models.IntegerField(default=0)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'


class Menu(models.Model):
    SEASON_SUMMER = 'summer'
    SEASON_WINTER = 'winter'

    SEASON_CHOICES = (
        (SEASON_SUMMER, "Summer Menu"),
        (SEASON_WINTER, "Winter Menu"),
    )

    title = models.CharField(max_length=50, null=False)
    season = models.CharField(
        max_length=30,
        choices=SEASON_CHOICES,
        default=SEASON_SUMMER,
        blank=True,
    )
    dishes = models.ManyToManyField(
        'restaurants.Dish',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
