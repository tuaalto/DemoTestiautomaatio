<<<<<<< HEAD
class Person:
    def __init__(self, city, address, phone_number, name, age):
        self.name = name
        self.age = age
        self._city = city
        self._address = address
        self._phone_number = phone_number

    @property
    def city(self, _default = None):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def phone_number(self, _default=None):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    def __str__(self):
        return f'Name: {self.name} Age: {self.age} Address: {self._address}\nCity: {self._city}\nPhone: {self._phone_number}'

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return name


