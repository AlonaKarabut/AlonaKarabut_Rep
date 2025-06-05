# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

testStringSet = set(input("Enter info: "))

for uniqueSymbol in testStringSet:
    if len(testStringSet) > 10:
        print(True)
    else:
        print(False)
    break

