#приближённо вычисляет площадь круга, используя случайные точки
import random  # модуль для генерации случайных чисел
import math    # модуль для математических функций

# функция вычисляет площадь круга методом Монте-Карло
def circle_square_mk(r, n):
    
    inside_circle = 0  # счетчик точек внутри круга
    
    # выполняем n экспериментов
    for _ in range(n):
        
        # генерируем случайную точку внутри квадрата
        x = random.uniform(0, r)
        y = random.uniform(0, r)
        
        # проверяем попадает ли точка внутрь круга
        if x**2 + y**2 <= r**2:
            inside_circle += 1
            
    # доля точек внутри круга
    # inside_circle / n ≈ площадь четверти круга / площадь квадрата
    
    # вычисляем площадь круга
    area = 4 * (inside_circle / n) * (r**2)
    
    return area


if __name__ == '__main__':
    
    radius = 10  # радиус круга
    
    # разные количества экспериментов
    attempts = [100, 1000, 10000, 100000]
    
    # точная площадь круга
    exact_area = math.pi * radius**2
    
    print(f"Exact Area: {exact_area:.4f}")
    
    # запускаем метод Монте-Карло для разных n
    for n in attempts:
        
        mk_area = circle_square_mk(radius, n)
        
        # вычисляем погрешность
        error = abs(mk_area - exact_area)
        
        print(f"n={n:6d}, MK Area={mk_area:.4f}, Error={error:.4f}")