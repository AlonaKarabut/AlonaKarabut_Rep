def factorial(x):
    if x <= 0:
        return "Entered value in <= 0"
    elif x == 1:
        return 1
    else:
        return (x * factorial(x - 1)) # функція запускатиметься щоразу заново поки ми не наткнемось на перепону (поки х не буде = 1)


def fact(number):
    item = 1
    result = 1
    while (item <= number):
        result = result * item
        item = item + 1
    return result

print(fact(6))

def factor(value):
    result = 1
    for num in range(1, value+1):   #  +1 тому що беремо range від 1 до value не включно
        result = result * num
    return result
