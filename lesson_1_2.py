class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.circumference = 2 * self.pi * self.radius

    def get_area(self):
        return self.pi * (self.radius ** 2)


circle_1 = Circle(4)
print(circle_1.get_area())
print(circle_1.circumference)
