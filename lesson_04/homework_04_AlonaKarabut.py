adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("task 01")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
print("\ntask 02")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("\ntask 03")
import re
adwentures_of_tom_sawer = re.sub(r'\s+', " ", adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("\ntask 04")
count_h = adwentures_of_tom_sawer.count("h")
print(count_h, "разів у тексті зустрічається літера \"h\".")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("\ntask 05")
list = adwentures_of_tom_sawer.split()

count = 0
for element in list:
    if element.istitle():
        count = count + 1

print(count, "слів у тексті починається з Великої літери")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("\ntask 06")
print("Позиція, на якій слово Tom зустрічається вдруге:", str(adwentures_of_tom_sawer.index("Tom", adwentures_of_tom_sawer.index("Tom") + 1))),
# index = find:
# print(adwentures_of_tom_sawer.find("Tom", adwentures_of_tom_sawer.find("Tom") + 1))

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("\ntask 07")

adwentures_of_tom_sawer_sentences1 = adwentures_of_tom_sawer.split("." or "!" or "?")
adwentures_of_tom_sawer_sentences = []
for sentence in adwentures_of_tom_sawer_sentences1:
    if sentence != "":
        cutspaces = sentence.strip()
        adwentures_of_tom_sawer_sentences.append(cutspaces)
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("\ntask 08")
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("\ntask 09")

for a in adwentures_of_tom_sawer_sentences:
    line = a.startswith("By the time")
    if line != -1:
        print("Є речення, що починається з \"By the time\"")
    else:
        print("Жодне речення не починається з \"By the time\"")
    break

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("\ntask 10")
print("Кількість слів останнього речення з adwentures_of_tom_sawer_sentences:", len((adwentures_of_tom_sawer_sentences[-1]).split()))