class Address:
    def __init__(self, city, street, house_number):
        self.__city = city
        self.__street = street
        self.__house_number = house_number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street):
        self.__street = street

    @property
    def house_number(self):
        return self.__house_number

    @house_number.setter
    def house_number(self, house_number):
        self.__house_number = house_number


class Animal:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.address = address
        self.__created()

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            print("Wrong value for age, it must be positive number")

    def __created(self):
        print("_____________")
        print(f"{self.name} was born")

    def info(self):
        return f'Name: {self.name} Age: {self.age} Address: {self.address.city}, ' \
               f'{self.address.street} Street, {self.address.house_number}'

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, address):
        Animal.__init__(self, name, age, address)

    def speak(self):
        print("The dog says woof")


class Cat(Animal):
    def __init__(self, name, age, address):
        Animal.__init__(self, name, age, address)

    def speak(self):
        print("The cat says meow")


class Fish(Animal):
    def __init__(self, name, age, address, living_environment):
        Animal.__init__(self, name, age, address)
        self.living_environment = living_environment

    def info(self):
        return super().info() + " Lives in: " + self.living_environment

    def speak(self):
        print("The fish says nothing")


# animal = Animal("Juny", 29)
# animal.age = -12
# print(f'Name: {animal.name} Age: {animal.age}')

dog = Dog("Spike", 2, Address("New York", "Nice Avenue", 21))
print(dog.info())

cat = Cat("Tom", 3, Address("LA", "First", 232))
print(cat.info())

fish = Fish("Freddy", 1, Address("New York", "Central Park", 1), "River")
print(fish.info())

animals = [dog, cat, fish]
for a in animals:
    a.speak()
