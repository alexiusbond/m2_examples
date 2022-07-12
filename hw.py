class Car:
    wheels = 5

class Truck(Car):
    wheels = 10

man = Truck()
Truck.wheels = 8
kamaz = Truck()
print(man.wheels + kamaz.wheels + Car.wheels)
