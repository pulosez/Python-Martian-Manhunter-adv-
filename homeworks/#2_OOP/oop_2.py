"""
2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
  a.class Person: Make the class with composition.
    class Arm: Make the class with composition.
  b.class CellPhone: Make the class with aggregation
    class Screen: Make the class with aggregation
"""


class Person:
    def __init__(self):
        right_arm = Arm('Right side')
        left_arm = Arm('Left side')
        self.arms = [right_arm, left_arm]


class Arm:
    def __init__(self, side):
        self.side = side


print(f'/----------#2.a----------/')
person = Person()
for arm in person.arms:
    print(arm.side)


class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, display_resolution):
        self.display_resolution = display_resolution


print(f'/----------#2.b----------/')
screen = Screen('2400x1080')
cellPhone = CellPhone(screen)
print(cellPhone.screen.display_resolution)
