"""
3. class Profile:
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
"""


class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.info = [self.name, self.last_name, self.phone_number, self.address,
                     self.email, self.birthday, self.age, self.sex]

    def __str__(self):
        return f'Person information: {self.info}'


profile = Profile('Evan', 'Black', '077 8474 5378', '64 Old Edinburgh Road BEESTON REGIS NR26 2YP',
                  'EvanBlack@gmail.com', '24/07/1988', '32', 'Male')
print(profile)
