print("\n" + "_____CONCATENATION_____")

"""КОНКАТЕНАЦІЯ"""
helloName = ["Hello", " Valerian"]
print(','.join(helloName))

name = "Valerian"
print(f'Hello, {name}')

print("Hello, {}".format(name))

greeting = "Hello"
print(greeting + ", " + name)

print("\n" + "_____SPLIT_____")
"""___________SPLIT___________"""
greeting = "Hello, Valerian!"
print(greeting.split(","))

greeting = "Hello, Valerian! Hello, Valerian!"
print(greeting.split(" ", 2))

print("\n" + "_____STRIP_____")
"""___________STRIP___________"""
greeting = "...Hello!..."
print(greeting.strip("."))
print(greeting.lstrip("."))
print(greeting.rstrip("."))

print("\n" + "_____REPLACE_____")
"""__________REPLACE__________"""
greeting = "Hello, Valerian!"
print(greeting.replace("Hello", "Good Bye"))

print("\n" + "____РОЗПАКОВУВАННЯ____")
"""_________РОЗПАКОВУВАННЯ_________"""

def greet(greeting, name):
    print(f'{greeting}{name}!')
inputData = ["Hello, ", "Valerian"]
greet(*inputData)

def personData(name, age):
    print(f'{name} is {age} years old')
info = {"name": "Valerian", "age": "29"}
personData(**info) # Если поставить одну звездочку выведет ключи, а не значения

print("___розпаковування списків___")
numbers = [1, 2, 3, 4, 5]
a, b, c, d, e = numbers  # должно быть то же кол-во переменных
print(c, d)
a, *rest = numbers
print(a)  # Output: 1
print(rest)   # Output: [2, 3, 4, 5]

print("___приклад використання___")
def calculateSum(*a):
    return sum(a)
numbers = [1, 2, 3, 4, 5]
print(calculateSum(*numbers))

print("___приклад використання (комбінування послідовностей)___")
hello = ["Hello"]
name = ["Valerian"]
print([*hello, *name])
print(','.join([*hello, *name]))

"""_________________________________ТЕОРІЯ________________________________________"""

"""______Статичний метод______Метод класу_______"""
class CarDriver:

    #Конструктор (викликається при створені екземпляру)
    def __init__(self, age):
        self.age = age

    #Атрибут класу
    colour = "Black"

    #Загальний метод (екземпляра)
    def start_engine(self):
        self.__supply_fuel()
        self.__ignite_spark()
        return "Двигун запущено"

    # Приватний метод (екземпляра)
    def __supply_fuel(self):
        print("Паливо подано")

    # Приватний метод (екземпляра)
    def __ignite_spark(self):
        print("Іскру подано")

    # Загальний Метод екземпляра (Instance method)
    def describe_driver(self):
        return f"I am {self.age} years old!"

    #Статичний метод   <<< це метод у класі, який не використовує self і працює як звичайна функція, але логічно належить до класу.
    @staticmethod
    def horn():
        return "Гудоооооок!"

    #Метод класу    <<<Може використовувати тільки атрибути класу
    @classmethod
    def describe_car(cls):   # <<<< Приймає cls — сам клас
        return f"My car is {cls.colour}"   # <<<< Приймає cls — сам клас


me = CarDriver(18)
you = CarDriver(20)

print(me.start_engine())
print(me.describe_car())

print(CarDriver.horn())   # <<< Викликається через клас або об'єкт — результат однаковий
print(me.horn())


"""____________Абстракції_____________"""
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):

    def speak(self):
        return "Chirik!"

bird = Bird()
print(bird.speak())

"""___________ABC______________"""
from abc import ABC, abstractmethod

# Абстрактний клас
class Figure(ABC):
    """Метод для обчислення площі"""
    @abstractmethod
    def area(self):
        pass

    """Метод для обчислення периметру"""
    @abstractmethod
    def perimeter(self):
        pass

# Конкретні реалізації (наслідування від абстрактного класу)
class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

rectangle = Rectangle(5, 10)

"""___________МРО_____________"""
class A:
    pass

class B(A):
    pass

class C():
    pass

class D(C, B):
    pass

print(D.__mro__)

"""_________________SOLID_____________"""

#DRY
#Don`t repeat yourself!

#KISS
#Keep it simple, Sir or Stupid!

#YAGNI
#You aren`t gonna need it!

#SOLID
#Це 5 принципів об'єктно-орієнтованого програмування, які допомагають писати чистий, зрозумілий і гнучкий код.

#S — Single Responsibility Principle  (Принцип єдиної відповідальності)
# Тварини - бувають риби, бувають звірі, бувають птахи. Погано всіх зводити до одного класу.

#Bad:

class Animal:

    def swim(self):
        pass

    def walk(self):
        pass

    def fly(self):
        pass


#Good:

class Animal:
    pass

class Fish(Animal):
    def swim(self):
        pass

class LandAnimal(Animal):
    def walk(self):
        pass

class Bird(Animal):
    def fly(self):
        pass

# O — Open/Closed Principle
# Клас має бути відкритим для розширення, але закритим для модифікації.


#Bad
class Animal:
    def make_sound(self, type):
        if type == "dog":
            return "Bark"
        elif type == "cat":
            return "Meow"
        elif type == "duck":
            return "Quack"




#Good
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Duck(Animal):
    def make_sound(self):
        return "Quack"


# L — Liskov Substitution Principle   (Принцип підстановки Барбари Лісков)
# Підкласи повинні повністю замінювати батьківський клас без неочікуваної поведінки.
#Підкласи повинні працювати так, щоб їх можна було використовувати замість батьківського класу без помилок.

#Bad
#Bird має метод fly(), але підклас Penguin не може літати
class Bird:
    def fly(self):
        pass

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly!")

#Good

class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        pass

class Ostrich(Bird):
    def run(self):
        pass


# I — Interface Segregation Principle     (Принцип розділення інтерфейсів)

# Краще кілька вузьких інтерфейсів, ніж один загальний з купою методів.
# Не змушуй клас реалізовувати методи, які йому не потрібні. Розділяй великі інтерфейси на менші

#Bad
class Animal:
    def fly(self):
        pass
    def walk(self):
        pass
    def swim(self):
        pass


#Good
class Swimmer:
    def swim(self):
        pass

class Walker:
    def walk(self):
        pass

class Flyer:
    def fly(self):
        pass

class Duck(Swimmer, Walker, Flyer):
    pass

class Fish(Swimmer):
    pass

# D — Dependency Inversion Principle     (Принцип інверсії залежностей)
# Високорівневі модулі не повинні залежати від деталей, а від абстракцій.
#Клас не повинен напряму залежати від конкретних реалізацій. Він має залежати від абстракції (інтерфейсу, базового класу).

#Bad
#У батьківському класі Animal уже є реалізація eat(), яка каже: «всі тварини їдять кості».
#Тобто клас вказує поведінку, яка не є універсальною, а це суперечить логіці і ускладнює підтримку коду.
class Animal():
    def eat(self):
        print("Їсть кості")

class Dog(Animal):
    pass

class Cat(Animal):
    def eat(self):
        print("Кіт їсть рибу")


from abc import ABC, abstractmethod

#Good
# Абстракція — загальний інтерфейс для всіх тварин
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

# Деталі — конкретні реалізації тварин
class Dog(Animal):
    def eat(self):
        print("Собака їсть корм")

class Cat(Animal):
    def eat(self):
        print("Кіт їсть рибу")