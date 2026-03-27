import csv

adult = 0
pensioner = 0
child = 0

with open("products.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # пропускаем заголовок
    for row in reader:
        adult += float(row[1])
        pensioner += float(row[2])
        child += float(row[3])

print(f"{adult:.2f} {pensioner:.2f} {child:.2f}")