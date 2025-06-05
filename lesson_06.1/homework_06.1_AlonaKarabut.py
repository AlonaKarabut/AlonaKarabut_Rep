# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

testString = set(input("Enter info: "))

if len(testString) > 10:
    print(True)
else:
    print(False)