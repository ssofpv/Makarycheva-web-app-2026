n, m = map(int, input().split())        # Читаем размеры (в Python часто не нужны для логики)
arr = list(map(int, input().split()))   # Читаем массив чисел
A = set(map(int, input().split()))      # Множество "хороших" чисел
B = set(map(int, input().split()))      # Множество "плохих" чисел
mood = 0

for x in arr:
    if x in A:      # Если число в множестве А
        mood += 1   # Настроение +1
    elif x in B:    # Если число в множестве B
        mood -= 1   # Настроение -1
print(mood) 