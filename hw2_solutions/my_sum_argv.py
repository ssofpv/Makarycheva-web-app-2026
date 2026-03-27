import sys
from my_sum import my_sum

if __name__ == '__main__':
    try:
        # Преобразуем аргументы командной строки в float, пропуская имя скрипта
        args = map(float, sys.argv[1:])
        print(my_sum(*args))
    except ValueError:
        print("Ошибка: Аргументы должны быть числами.")