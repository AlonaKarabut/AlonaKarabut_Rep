# Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".


while False:
    enteredWord = input("Enter word containing letter 'h': ")
    if "h" in enteredWord or "H" in enteredWord:
        print("Thank you, good job!")
        break
    else:
        print("Sorry, you entered word containing no letter 'h'. Try again.")