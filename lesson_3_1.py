class MusicPlayable:
    def play_music(self, song):
        print(f'Now is playing  {song} song')


class Car(MusicPlayable):
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    def drive(self):
        print("I can drive")

    def __str__(self):
        return f'Car\n' \
               f'Model: {self.model} Year: {self.year} '

    def __gt__(self, other):
        return self.__year > other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

    def __le__(self, other):
        return self.__year <= other.__year


class ElectricCar(Car):
    def __init__(self, model, year, battery):
        Car.__init__(self, model, year)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, battery):
        self.battery = battery

    def drive(self):
        print("I can drive using electric engine")

    def __str__(self):
        return super(ElectricCar, self).__str__() + f' Battery: {self.battery}'


class FuelCar(Car):
    __total_fuel = 500

    def __init__(self, model, year, fuel_amount):
        Car.__init__(self, model, year)
        self.__fuel_amount = fuel_amount

    @staticmethod
    def print_fuel_type():
        print("AI 98")

    @classmethod
    def put_fuel(cls, car, amount):
        cls.__total_fuel -= amount
        print(f'Total fuel remain: {cls.__total_fuel}')
        car.fuel_amount += amount

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, fuel_amount):
        self.__fuel_amount = fuel_amount

    def drive(self):
        print("I can drive using fuel engine")

    def __str__(self):
        return super(FuelCar, self).__str__() + f' Fuel amount: {self.fuel_amount}'

    def __add__(self, other):
        return self.fuel_amount + other.fuel_amount


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, battery, fuel_amount):
        ElectricCar.__init__(self, model, year, battery)
        FuelCar.__init__(self, model, year, fuel_amount)


class SmartPhone(MusicPlayable):
    pass


prius = HybridCar("Toyota Prius", 2011, 80000, 35)
print(prius)
prius.drive()
print(HybridCar.mro())
FuelCar.put_fuel(prius, 9)
print(prius)

honda = FuelCar("Honda Fit", 2020, 45)
print(honda)
FuelCar.put_fuel(honda, 10)
print(honda)
honda.play_music('Hello song')

phone = SmartPhone()
phone.play_music("Good morning")

print(honda <= prius)
print(honda + prius)
# print(honda - prius)
