n = int(input())            # Количество интервалов
cnt = 0
intervals = []

# 1. Запоминаем все интервалы
for _ in range(n):
    a, b = map(int, input().split()) 
    intervals.append((a, b))

# 2. Читаем проверочное число T
T = int(input())

# 3. Проверяем, сколько интервалов "накрывают" число T
for a, b in intervals:
    if a <= T <= b:         # Если T находится между a и b включительно
        cnt += 1
print(cnt) 