# task 1
print("Task 1")
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number):
    """
    Функція друкує табличку множення на задане число, але
    лише до максимального значення для добутку - 25.
    """
    multiplier = 1
    while True:
        result = number * multiplier
        multiplier = multiplier + 1
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

multiplication_table(3)

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
print("\nTask 2")
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sumOfTwoNumbers(a, b):
    """
    Функція, обчислює суму двох чисел
    """
    result = a + b
    return(result)

print(sumOfTwoNumbers(4, 7))

# task 3
print("\nTask 3")
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def countAverage(*args):
    """
    Функція розрахує середнє арифметичне списку чисел
    """
    newList = []
    for arg in args:
        newList.append(arg)
    average = sum(newList) / len(newList)
    return(average)

print(countAverage(6, 2, 4))

# task 4
print("\nTask 4")
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def lineToRevert():
    """
    Функція приймає рядок та повертає його у зворотному порядку.
    """
    input_line = input("Enter a string: ")
    return input_line[::-1]

print(lineToRevert())

# task 5
print("\nTask 5")
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def findLongestWord():
    """
    Функція приймає список слів та повертає найдовше слово у списку.
    """
    input_str = input("Enter words separated by space: ")
    words = input_str.split(" ")
    longestWord = max(words, key=len)
    return longestWord

print(findLongestWord())

# task 6
print("\nTask 6")
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    """
    Функція приймає два рядки та повертає індекс першого входження другого рядка
    у перший рядок (або -1, якщо другий рядок не є підрядком першого рядка).
    """
    if str1.find(str2) != -1:
        return str1.index(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
print("\nTask 7")
"""Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
Данні в лісті можуть бути будь якими"""

def returnStringsOnly():
    """
    Функція формує новий list (lst2) для заданного list з даними (lst1),
    який містить лише змінні типу стрінг, які присутні в lst1.
    """
    list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
    list2 = []
    for a in list1:
        if type(a) == str:
            list2.append(a)
    return(list2)

print(returnStringsOnly())

# task 8
print("\nTask 8")
"""Напишіть цикл, який буде вимагати від користувача ввести слово,
в якому є літера "h" (враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h"."""

def enterWordWithH():
    """
    Функція вимагає від користувача ввести слово, в якому є літера "h"
    (враховуються як великі так і маленькі),
    і цикл не завершується допоки умова не буде виконана.
    """
    while True:
        enteredWord = input("Enter word containing letter 'h': ")
        if "h" in enteredWord or "H" in enteredWord:
            print("Thank you, good job!")
            break
        else:
            print("Sorry, you entered word containing no letter 'h'. Try again.")

enterWordWithH()

# task 9
print("\nTask 9")
"""Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()"""

def countUniqueSymbols():
    """
    Функція рахує кількість унікальних символів в строці і виводить True якщо їх більше 10. Інакше - False.
    """
    testString = set(input("Enter info: "))
    for uniqueSymbol in testString:
        if len(testString) > 10:
            print(True)
        else:
            print(False)
        break

countUniqueSymbols()

# task 10
print("\nTask 10")
"""Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті"""
def sumOfAllEvenNumbers():
    Numbers = [1, 3, 5, 8, 2, 39, 100]
    Result = []
    for a in Numbers:
        if a % 2 == 0:
            Result.append(a)
    return(sum(Result))

print(sumOfAllEvenNumbers())

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""