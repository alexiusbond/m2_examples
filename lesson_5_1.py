from random import randint as generate_number
from person import Person
import calculator
from datetime import date, datetime
from termcolor import colored, cprint
import os
from envparse import env

print(generate_number(1, 7))

print(calculator.addition(2, 5))

print(Person("John", 23))

yesterday = date(2022, 5, 16)
today = date.today()
print(f'Yesterday date: {yesterday} + day of the week: {yesterday.weekday()}')
print(today > yesterday)
print(today.strftime("%Y %b %d (%a)"))

now = datetime.now()
print(now)

deadline = datetime.strptime("22/05/2017", "%d/%m/%Y")
print(deadline)  # 2017-05-22 00:00:00

cprint("hello", "green", attrs=['underline', 'dark'])
print(colored("Python", "red"))

print(os.environ.get('LESSON_5'))
env.read_envfile('opts.env')
print(os.environ.get('GEEKTECH'))
