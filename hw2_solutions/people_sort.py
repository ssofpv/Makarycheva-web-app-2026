#сортировка людей по возрасту и красиво
import operator

# декоратор для сортировки списка людей
def person_lister(f):
    
    # внутренняя функция
    def inner(people):
        
        # people — список людей
        # каждый человек — список: [name, surname, age, sex]
        
        # сортируем по возрасту (индекс 2)
        people.sort(key=lambda x: int(x[2]))
        
        # применяем функцию форматирования к каждому элементу
        return map(f, people)
        
    return inner


# применяем декоратор
@person_lister
def name_format(person):
    
    # если пол мужской
    if person[3] == "M":
        title = "Mr. "
    else:
        title = "Ms. "
        
    # возвращаем отформатированное имя
    return title + person[0] + " " + person[1]


if __name__ == '__main__':
    
    try:
        # считываем количество людей
        people = [input().split() for i in range(int(input()))]
        
        # выводим результат
        print(*name_format(people), sep='\n')
        
    except (ValueError, IndexError):
        pass