# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

Numbers = [1, 3, 5, 8, 2, 39, 100]

Result = []

for a in Numbers:
    if a%2 == 0:
        Result.append(a)
print(sum(Result))