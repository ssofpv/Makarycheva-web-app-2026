n, m = map(int, input().split()) # n = вместимость рюкзака, m = кол-во предметов
items = []

# 1. Сбор данных
for _ in range(m):
    name, w, c = input().split()
    w = float(w); c = float(c)
    # Сохраняем: [Имя, Вес, Цена, Цена_за_1кг]
    items.append([name, w, c, c/w])

# 2. Сортировка по "выгодности" (Цена за 1кг)
# reverse=True значит от самого дорогого к дешевому
items.sort(key=lambda x: x[3], reverse=True)

res = []
cap = n  # Оставшееся место в рюкзаке

# 3. Наполнение рюкзака
for name, w, c, ratio in items:
    if cap <= 0: 
        break # Рюкзак полон, выходим
    
    take = min(w, cap) # Берем либо весь предмет, либо сколько влезает
    res.append((name, take, take * ratio)) # Записываем, сколько взяли и по какой цене
    cap -= take # Уменьшаем свободное место

# 4. Вывод результата
for name, w, c in res:
    print(f"{name} {w:.2f} {c:.2f}") 