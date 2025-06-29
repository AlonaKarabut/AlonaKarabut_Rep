# Створіть клас Employee, який має атрибути name та salary.
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників.
# Клас TeamLead повинен мати всі атрибути як Manager (ім('я, зарплата, відділ), '
# а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size

"""Next option is also possible but it ignores MRO and may call Employee.__init__ twice, so Super is prefferable"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, team_size):
        Manager.__init__(self, name, salary, department)
        self.team_size = team_size

# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def Area(self):
        pass

    @abstractmethod
    def Perimeter(self):
        pass

class Square(Figure):

    def __init__(self, side):
        self.side = side

    def Area(self):
        return f"Square Area is {self.side ** 2}"

    def Perimeter(self):
        return f"Square Perimeter is {self.side * 4}"

class Rectangle(Figure):

    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def Area(self):
        return f"Rectangle Area is {self.side1 * self.side2}"

    def Perimeter(self):
        return f"Rectangle Perimeter is {(self.side1 + self.side2) * 2}"

class Parallelogram(Figure):

    def __init__(self, side1, side2, height):
        self.side1 = side1
        self.side2 = side2
        self.height = height

    def Area(self):
        return f"Parallelogram Area is {self.side1 * self.height}"

    def Perimeter(self):
        return f"Parallelogram Perimeter is {(self.side1 + self.side2) * 2}"

square = Square(5)
print(square.Area())
print(square.Perimeter())

rectangle = Rectangle(4, 2)
print(rectangle.Area())
print(rectangle.Perimeter())

parallelogram = Parallelogram(3, 5, 2)
print(parallelogram.Area())
print(parallelogram.Perimeter())