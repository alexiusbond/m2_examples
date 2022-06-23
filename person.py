class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def __str__(self):
        return f'Name: {self.name} Age: {self.age}'


if __name__ == '__main__':
    print(Person("Ali", 11))
