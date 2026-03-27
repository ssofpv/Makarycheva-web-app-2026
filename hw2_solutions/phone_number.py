#Программа демонстрирует использование декораторов и сортировки списков.
# декоратор для предварительной обработки номеров

def wrapper(f):
    
    def fun(l):
        
        formatted_numbers = []  # список отформатированных номеров
        
        # обрабатываем каждый номер
        for number in l:
            
            # оставляем только цифры
            digits = ''.join(filter(str.isdigit, number))
            
            # берем последние 10 цифр
            ten_digits = digits[-10:]
            
            # форматируем номер
            fmt = "+7 ({}) {}-{}-{}".format(
                ten_digits[:3],     # код оператора
                ten_digits[3:6],    # первая часть
                ten_digits[6:8],    # вторая часть
                ten_digits[8:]      # последняя часть
            )
            
            formatted_numbers.append(fmt)
        
        # вызываем функцию сортировки
        return f(formatted_numbers)
    
    return fun


# применяем декоратор
@wrapper
def sort_phone(l):
    
    # сортируем номера
    return sorted(l)


if __name__ == '__main__':
    
    try:
        # читаем номера
        l = [input() for _ in range(int(input()))]
        
        # выводим результат
        print(*sort_phone(l), sep='\n')
        
    except (ValueError, IndexError):
        pass