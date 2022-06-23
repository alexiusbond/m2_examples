class Transport:

    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def change_color(self, new_color):
        self.color = new_color
        print(f'Color changed to {new_color}')


class Rocket(Transport):

    def __init__(self, model, color, year):
        Transport.__init__(self, model, color, year)

    def fly(self, planet):
        print(f'Rocket {self.model} is flying to {planet}')


class Car(Transport):
    number_of_wheels = 4

    def __init__(self, model, color, year, penalties=0):
        Transport.__init__(self, model, color, year)
        self.penalties = penalties

    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    number_of_wheels = 8

    def __init__(self, model, color, year, penalties, load_capacity):
        Car.__init__(self, model, color, year, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, weight):
        if weight <= self.load_capacity:
            self.load_capacity -= weight
            print(f'The cargo is loaded. Remains load capacity of {self.load_capacity}kg')
        else:
            print(f'You can not load more than {self.load_capacity}')


falcon_rocket = Rocket("Falcon 9", "White", 2011)
print(f'{falcon_rocket.model} {falcon_rocket.color} {falcon_rocket.year}')
falcon_rocket.fly("Mars")
falcon_rocket.change_color("Blue")
print(f'{falcon_rocket.model} {falcon_rocket.color} {falcon_rocket.year}')

mazda_car = Car(model="Mazda CX7", color="red", year=2001, penalties=500)
print(f'{mazda_car.model} {mazda_car.color} {mazda_car.year} {mazda_car.penalties} '
      f'{mazda_car.number_of_wheels}')
mazda_car.drive("Miami")

winter_tires = Car.number_of_wheels * 5
print(f'We need {winter_tires} tires for winter season')

bmw_car = Car("BMW 5", "red", 2017)
bmw_car.number_of_wheels = 5
print(f'{bmw_car.model} {bmw_car.color} {bmw_car.year} {bmw_car.penalties} '
      f'{bmw_car.number_of_wheels}')
bmw_car.penalty_amount = 1000
print(f'{bmw_car.model} {bmw_car.color} {bmw_car.year} {bmw_car.penalty_amount} {bmw_car.number_of_wheels}')
Car.number_of_wheels = 5
honda_car = Car("Honda CRV", "silver", 2020, 0)
print(f'{honda_car.model} {honda_car.color} {honda_car.year} {honda_car.penalties} {honda_car.number_of_wheels}')
honda_car.drive("Osh")
honda_car.change_color("blue")
print(f'{honda_car.model} {honda_car.color} {honda_car.year} {honda_car.penalties} '
      f'{honda_car.number_of_wheels}')

man_truck = Truck("Man 212", "white", 2020, 900, 20000)
print(
    f'{man_truck.model} {man_truck.color} {man_truck.year} '
    f'{man_truck.penalties} {man_truck.load_capacity} {man_truck.number_of_wheels}')
man_truck.drive("Los Angeles")
man_truck.load_cargo(500000)
man_truck.load_cargo(3000)
