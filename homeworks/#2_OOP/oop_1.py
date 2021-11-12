"""
1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class
    class Animals:
        Parent class, should have eat, sleep
    class Animal1(Animal):
        Some of the animal with 1-2 extra methods related to this animal
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.__class__.__name__} {self.name} is eating')

    def sleep(self):
        print(f'{self.__class__.__name__} {self.name} is sleeping')


class Cat(Animal):
    def drink_milk(self):
        print(f'{self.__class__.__name__} {self.name} is drinking milk')


class Dog(Animal):
    def run(self):
        print(f'{self.__class__.__name__} {self.name} is running')


class Owl(Animal):
    def fly(self):
        print(f'{self.__class__.__name__} {self.name} is flying')


class Rabbit(Animal):
    def jump(self):
        print(f'{self.__class__.__name__} {self.name} is jumping')


class Wolf(Animal):
    def hunt(self):
        print(f'{self.__class__.__name__} {self.name} is hunting')

    def miss(self):
        print(f'{self.__class__.__name__} {self.name} has missed')


cat = Cat('Murka')
dog = Dog('Jack')
owl = Owl('Hedwig')
rabbit = Rabbit('Roger')
wolf = Wolf('Akela')

print(f'/----------#1----------/')
cat.drink_milk()
dog.run()
owl.fly()
rabbit.jump()
wolf.hunt()
wolf.miss()

print(f'Determine if each of the animal is an instance of the Animals class:')
print(f'cat: {isinstance(cat, Animal)}')
print(f'dog: {isinstance(dog, Animal)}')
print(f'owl: {isinstance(owl, Animal)}')
print(f'rabbit: {isinstance(rabbit, Animal)}')
print(f'wolf: {isinstance(wolf, Animal)}')

"""
1.a. Create a new class Human and use multiple inheritance to create Centaur class,
 create an instance of Centaur class and call the common method of these classes and unique.
 
 class Human:
    Human class, should have eat, sleep, study, work
 class Centaur(.. , ..):
    Centaur class should be inherited from Human and Animal and has unique method related to it.
"""


class Human:
    def __int__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.__class__.__name__} {self.name} is eating')

    def sleep(self):
        print(f'{self.__class__.__name__} {self.name} is sleeping')

    def study(self):
        print(f'{self.__class__.__name__} {self.name} is studying')

    def work(self):
        print(f'{self.__class__.__name__} {self.name} is working')


class Centaur(Human, Animal):
    def gallop(self):
        print(f'{self.__class__.__name__} {self.name} is galloping')

    def fight(self):
        print(f'{self.__class__.__name__} {self.name} is fighting')


print(f'/----------#1.a----------/')
centaur = Centaur('Chiron')
centaur.eat()
centaur.sleep()
centaur.study()
centaur.work()
centaur.gallop()
centaur.fight()
