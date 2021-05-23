from abc import ABC, abstractmethod
import random


class Human(ABC):
    @abstractmethod
    def provide_info(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self, *args, **kwargs):
        raise NotImplementedError


class Person(Human):
    def __init__(self, name, age, money_availability, home_having=[]):
        self.name = name
        self.age = age
        self.money_availability = money_availability
        self.home_having = home_having

    def provide_info(self):
        print(f'\n-----Person information:-----\n'
              f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'Money: {self.money_availability}\n'
              f'Houses:')
        for house in self.home_having:
            print(f'#{self.home_having.index(house)}: {str(house)}')

    def make_money(self, salary: (int, float)):
        print(f'Person {self.name} has {self.money_availability}')
        self.money_availability += salary
        print(f'{self.name} make money. Now the amount of money is equal {self.money_availability}')

    def buy_house(self, house, realtor):
        print(f'Person {self.name} trying to buy new house: {str(house)}')
        if house in realtor.houses:
            if house.cost <= self.money_availability:
                if realtor.steal_money() <= 10:
                    self.money_availability -= house.cost
                    print(f'Realtor {realtor.name} stole money. Now {self.name} has {self.money_availability}')
                else:
                    print(f'Realtor {realtor.name} did not steal money')
                    realtor.houses.remove(house)
                    self.money_availability -= house.cost
                    self.home_having.append(house)
                    print(f'Person {self.name} bought house with cost {house.cost}')
            else:
                print(f'Person {self.name} does not have enough money')
        else:
            print(f'There is no such house in the list')


class Home(ABC):
    @abstractmethod
    def apply_discount(self, *args, **kwargs):
        raise NotImplementedError


class House(Home):
    def __init__(self, cost, area):
        self.cost = cost
        self.area = area

    def apply_discount(self, discount):
        self.cost *= 1 - discount / 100

    def __str__(self):
        return f'Cost {self.cost}, Area {self.area}m2'


class SmallHouse(House):
    def __init__(self, cost, area=40):
        super().__init__(cost, area)


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, discount, houses=[]):
        self.name = name
        self.discount = discount
        self.houses = houses

    def provide_info_about_houses(self):
        print(f'\n-----Realtor {self.name} sells such houses:-----')
        for house in self.houses:
            print(f'#{self.houses.index(house)}: {str(house)}')

    def give_discount(self, house):
        if house in self.houses:
            print(f'Realtor {self.name} can give a discount of {self.discount}%')
            house.apply_discount(self.discount)
            print(f'Price after discount is {house.cost}')
        else:
            print(f'There is no such house in the list')

    def steal_money(self):
        return random.randrange(0, 100)


"""
    def steal_money(self, person, house):
        if random.randrange(0, 100) <= 10:
            person.money_availability -= house.cost
            print(f'Realtor {self.name} stole money. Now {person.name} has {person.money_availability}')
"""
if __name__ == "__main__":
    house0 = House(22000.0, 55)
    house1 = House(20000.0, 45)
    house2 = SmallHouse(17000.0)
    house3 = House(40000.0, 75)

    person0 = Person('John', 27, 20000.0, [house1])
    person0.provide_info()

    realtor0 = Realtor('Jane', 15.0, [house2, house3])
    realtor0.provide_info_about_houses()

    print('\n')
    person0.buy_house(house0, realtor0)
    person0.buy_house(house3, realtor0)
    person0.make_money(22000.0)
    realtor0.give_discount(house2)
    realtor0.give_discount(house3)
    person0.buy_house(house3, realtor0)

    person0.provide_info()
    realtor0.provide_info_about_houses()
