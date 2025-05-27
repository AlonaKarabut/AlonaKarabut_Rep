alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."\n')
print("task 01-03")
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
print("task 04")
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
BlackSea = 436402
SeaOfAzov = 37800
Total = BlackSea + SeaOfAzov
print("Total area of two sees is" + " " + str(Total) + " " + "km\n")

# task 05
print("task 05")
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
TotalGoods = 375291
Warehouse1and2 = 250449
Warehouse2and3 = 222950
Warehouse1 = TotalGoods - Warehouse2and3
Warehouse2 = Warehouse1and2 - Warehouse1
Warehouse3 = TotalGoods - Warehouse1and2
print(str(Warehouse1) + " " + "items are stored in the first warehouse")
print(str(Warehouse2) + " " + "items are stored in the second warehouse")
print(str(Warehouse3) + " " + "items are stored in the third warehouse\n")

# task 06
print("task 06")
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
MonthlyPay = 1179
Time = 18
Price = MonthlyPay * Time
print("Computer price is" + " " + str(Price) + " " + "UAH\n")

# task 07
print("task 07")
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("The remainder of dividing 8019 by 8 is" + " " + str(8019 % 8))
print("The remainder of dividing 9907 by 9 is" + " " + str(9907 % 9))
print("The remainder of dividing 2789 by 5 is" + " " + str(2789 % 5))
print("The remainder of dividing 7248 by 6 is" + " " + str(7248 % 6))
print("The remainder of dividing 7128 by 5 is" + " " + str(7128 % 5))
print("The remainder of dividing 19224 by 9 is" + " " + str(19224 % 9))

# task 08
print("\ntask 08")
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

BigPizza = 274 * 4
MediumSizePizza = 218 * 2
Juice = 35 * 4
Cake = 350
Water = 21 * 3
Total = BigPizza + MediumSizePizza + Juice + Cake + Water
print("Irynka is about to spend" + " " + str(Total) + " " + "UAH on her B-day\n")

# task 09
print("task 09")
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
Photos = 232
PhotosOnPage = 8
Pages = Photos / PhotosOnPage
print("Ihor will need" + " " + str(round(Pages)) + " " + "pages of album for all his photos\n")

# task 10
print("task 10")
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
Distance = 1600
GasPer100km = 9
GasTank = 48

TotalGasNeeded = Distance / 100 * GasPer100km
Refueling = int(TotalGasNeeded) / GasTank

print("1)" + " " + str(round(TotalGasNeeded)) + " " + "liters of Gas is needed for the whole trip")
print("2)" + " " + str(round(Refueling)) + " " + "refuelings are needed on the trip")