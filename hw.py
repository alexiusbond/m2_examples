class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def introducemyself(self):
        print(f"my name is {self.fullname}, i am {self.age} years old and {self.is_married}")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks, math, english, physics, russian):
        super().__init__(fullname, age, is_married)
        self.marks = marks
        self.marks ={ math: 3, english: 5, physics: 4, russian: 4 }

    def averagemarks(self, math, english, physics, russian):
        print((math+english+physics+russian)/4)

ilya = Student("Shtelya Ilya", 18,"not married", "good", 3 , 4, 5, 3)

ilya.averagemarks(3, 4, 5, 3)

class Teacher(Person):
    salary = 10000
    def __init__(self, fullname, age, is_married, expirience):
        super().__init__(fullname, age, is_married)
        self.expirience = expirience

    def salaryup(self, salary, expirience):
        if expirience>3:
            print(salary+((salary/100*5)*expirience))
        else:
            print("not enough expirience")

alexey = Teacher("Alexey", 34, "married", 4)
print(f'{alexey.fullname}, {alexey.age},{alexey.is_married}')
alexey.salaryup(10000, 4)

def create_students():
    list1 = list()
    n1 = Student("Alibek",17, "not married", "good", 3, 4, 5, 4)
    list1.append(n1)
    n2= Student("Jonybek", 16, "not married", "good", 4, 4, 5, 4)
    list1.append(n2)
    n3 = Student("Beckjan", 18, "married", "very good", 5, 5, 5, 4)
    list1.append(n3)
    return list1

create_students()