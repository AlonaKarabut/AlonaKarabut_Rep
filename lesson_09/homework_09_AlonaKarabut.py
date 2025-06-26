# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". 
# Створіть об'єкт цього класу, представляючий студента. 
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента. 
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, name, surname, age, grade):
        self.name = name
        self.surname = surname 
        self.age = age
        self.grade = grade

    def greet(self):
        return f"My name is {self.name} {self.surname}, I`m {self.age}. My current grade is {self.grade}.\n"

    def change_grade(self, new_grade):
        self.grade = new_grade
        return f"My new grade is {new_grade}."
        

student = Student("Alona", "Karabut", 28, 95)
student2 = Student("Valerian", "Hulpak", 29, 98)
student3 = Student("Vasyl", "Hulpak", 33, 96)


print(student.greet())
print(student.change_grade(100))

print(student2.greet())
print(student2.change_grade(99))

print(student3.greet())
print(student3.change_grade(98))