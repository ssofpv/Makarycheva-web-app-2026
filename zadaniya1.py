# Задание 1
def square(x):
    """Возвращает квадрат числа"""
    return x ** 2


# Задание 2
def is_even(x):
    """Возвращает True, если число четное, иначе False"""
    return x % 2 == 0


# Задание 3
def factorial(n):
    """Возвращает факториал числа"""
    if n < 0:
        return None  # Факториал определен только для неотрицательных чисел
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Задание 4
def greet(name):
    """Печатает приветствие"""
    print(f"Привет, {name}!")


# Задание 5
def add_numbers(a, b):
    """Возвращает сумму двух чисел"""
    return a + b


# Задание 6
def find_max(a, b, c):
    """Возвращает максимальное из трех чисел"""
    return max(a, b, c)


# Задание 7
def fibonacci(n):
    """Возвращает n-е число Фибоначчи"""
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Задание 8
def is_prime(n):
    """Проверяет, является ли число простым"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Примеры использования:
if __name__ == "__main__":
    # Тестируем функции
    print("Задание 1 (square):", square(5))  # 25
    
    print("Задание 2 (is_even):", is_even(4))  # True
    print("Задание 2 (is_even):", is_even(7))  # False
    
    print("Задание 3 (factorial):", factorial(5))  # 120
    
    print("Задание 4 (greet):")
    greet("Анна")  # Привет, Анна!
    
    print("Задание 5 (add_numbers):", add_numbers(3, 7))  # 10
    
    print("Задание 6 (find_max):", find_max(10, 5, 8))  # 10
    
    print("Задание 7 (fibonacci):", fibonacci(6))  # 8
    
    print("Задание 8 (is_prime):", is_prime(7))  # True
    print("Задание 8 (is_prime):", is_prime(10))  # False