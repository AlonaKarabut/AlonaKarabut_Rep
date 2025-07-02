def sumStringNumbers():
    """Функція обробляє список рядків, де числа розділені комами.
    Для кожного елемента обчислює суму чисел.
    Якщо рядок містить нечислові символи — виводить 'Не можу це зробити!'."""
    listWithStrings = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
    newList = []

    for string in listWithStrings:
        try:
            numbers = [int(x) for x in string.split(",")]
            newList.append(sum(numbers))
        except ValueError:
            newList.append("Не можу це зробити!")

    return newList

print(sumStringNumbers())


def sumOfAllEvenNumbers():
    """Функція обробляє ліст - виводить суму усіх ПАРНИХ чисел"""
    Numbers = [1, 3, 5, 8, 2, 39, 100]
    Result = []
    for a in Numbers:
        if a % 2 == 0:
            Result.append(a)
    return(sum(Result))

print(sumOfAllEvenNumbers())

def countUniqueSymbols():
    """
    Функція рахує кількість унікальних символів в строці і виводить True якщо їх більше 10. Інакше - False.
    """
    testString = set(input("Enter info: "))
    for uniqueSymbol in testString:
        if len(testString) > 10:
            return True
        else:
            return False
        break

if __name__ == "__main__":
    print(countUniqueSymbols())

def enterWordWithH():
    """
    Функція вимагає від користувача ввести слово, в якому є літера "h"
    (враховуються як великі так і маленькі),
    і цикл не завершується допоки умова не буде виконана.
    """
    while True:
        enteredWord = input("Enter word containing letter 'h': ")
        if "h" in enteredWord or "H" in enteredWord:
            return "Thank you, good job!"
            break
        else:
            return "Sorry, you entered word containing no letter 'h'. Try again."


if __name__ == "__main__":
    print(enterWordWithH())

def findLongestWord():
    """
    Функція приймає список слів та повертає найдовше слово у списку.
    """
    input_str = input("Enter words separated by space: ")
    words = input_str.split(" ")
    longestWord = max(words, key=len)
    return longestWord

if __name__ == "__main__":
    print(findLongestWord())