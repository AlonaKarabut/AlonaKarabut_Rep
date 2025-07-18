# Генератори:
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
print("Генератор, який повертає послідовність парних чисел від 0 до N")

def even_numbers_generator(N):
    for num in range (0, N + 1):
        if isinstance(num, int) and num != 0 and num % 2 ==0:
            yield num

even = even_numbers_generator(8)

print(next(even))
print(next(even))
print(next(even))
print(next(even))


# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
print("\nГенератор, який генерує послідовність Фібоначчі до певного числа N")

def fibonacci_generator(N):
    a, b = 0, 1
    flag = 0
    while flag <= N:
        yield a
        a, b = b, a + b
        flag += 1

fib = fibonacci_generator(7)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

# Ітератори:
# Реалізуйте ітератор для зворотного виведення елементів списку.
print("\nІтератор для зворотного виведення елементів списку")

def backwards_list_iterator(list):
    new_list = list[::-1]
    iterator = iter(new_list)
    return iterator

my_list = ["a", "b", "c"]
result = backwards_list_iterator(my_list)
print(next(result))
print(next(result))
print(next(result))

# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
print("\nІтератор,який повертає всі парні числа в діапазоні від 0 до N")

class ReturnEvenNumbersIterator:
    def __init__(self, N):
        self.N = N
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < self.N+1:
            if self.current != 0 and self.current % 2 == 0:
                even_number = self.current
                self.current += 1
                return even_number
            self.current += 1
        raise StopIteration

even_number = ReturnEvenNumbersIterator(12)

print(next(even_number))
print(next(even_number))
print(next(even_number))
print(next(even_number))
print(next(even_number))
print(next(even_number))


# Декоратори:
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
print("\nДекоратор, який логує аргументи та результати викликаної функції")

def log_arguments_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції: {func.__name__}")
        print(f"Аргументи: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@log_arguments_and_result
def sum_numbers(a, b):
    result = a + b
    return result

print(sum_numbers(1, b = 3))

# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
print("\nДекоратор,  який перехоплює та обробляє винятки, які виникають в ході виконання функції")

def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка у функції '{func.__name__}': {e}")
            return "Exception, read above"
    return wrapper

@catch_exceptions
def sum_numbers(a, b):
    result = a + b
    return result

print(sum_numbers(1, "d"))
