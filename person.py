class person():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return name

    def __str__(self):
        return (f"{name} is {age} years old.")
    

