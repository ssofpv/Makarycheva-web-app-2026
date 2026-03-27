def square(x):
    return x * x


def is_even(x):
    return x % 2 == 0


def factorial(n):
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def greet(name):
    print(f"Привет, {name}!")


def add_numbers(a, b):
    return a + b


def find_max(a, b, c):
    return max(a, b, c)


def fibonacci(n):
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    print("--- ЗАПУСК 8 ФУНКЦИЙ ---")

    # 1. Приветствие (сразу передаем ввод в функцию)
    greet(input("\n1. Введите имя: "))

    # 2. Квадрат
    n = int(input("\n2. Число для квадрата: "))
    print(f"Результат: {square(n)}")

    # 3. Четность (выведет True или False)
    n = int(input("\n3. Число для проверки на четность: "))
    print(f"Четное? {is_even(n)}")

    # 4. Факториал
    n = int(input("\n4. Число для факториала: "))
    print(f"Факториал: {factorial(n)}")

    # 5. Сложение (вводим и сразу считаем)
    print("\n5. Сложение")
    res = add_numbers(int(input("Число А: ")), int(input("Число Б: ")))
    print(f"Сумма: {res}")

    # 6. Максимум
    print("\n6. Поиск максимума")
    res = find_max(int(input("А: ")), int(input("Б: ")), int(input("В: ")))
    print(f"Максимум: {res}")

    # 7. Фибоначчи
    n = int(input("\n7. Номер числа Фибоначчи: "))
    print(f"Значение: {fibonacci(n)}")

    # 8. Простое число
    n = int(input("\n8. Число для проверки на простоту: "))
    print(f"Простое? {is_prime(n)}")