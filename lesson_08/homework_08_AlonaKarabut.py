"""Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
Використовуйте блок try except, щоб уникнути інших символів, окрім чисел у списку.
Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”"""


def sumStringNumbers():
    try:
        listWithStrings = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
        newList = []
        for string in listWithStrings:
            string = string.split(",")
            l = []
            for number in string:
                number1 = int(number)
                l.append(number1)
                result = sum(l)
        newList.append(result)
    except Exception:
        newList.append("Не можу це зробити")
    finally:
        print(newList)


sumStringNumbers()
