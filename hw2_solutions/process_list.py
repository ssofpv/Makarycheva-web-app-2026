import timeit

def process_list(arr):
    # Исходная реализация с list comprehension
    return [i**2 if i % 2 == 0 else i**3 for i in arr]

def process_list_gen(arr):
    # Реализация с генератором
    for i in arr:
        if i % 2 == 0:
            yield i**2
        else:
            yield i**3

if __name__ == '__main__':
    test_arr = list(range(1000))
    
    # Замер list comprehension
    t_list = timeit.timeit(lambda: process_list(test_arr), number=1000)
    
    # Замер генератора (преобразование в список для честного сравнения вычислений)
    t_gen = timeit.timeit(lambda: list(process_list_gen(test_arr)), number=1000)
    
    print(f"List comprehension time: {t_list:.6f}")
    print(f"Generator time: {t_gen:.6f}")

    # КОММЕНТАРИЙ О СРАВНЕНИИ:
    # List comprehension обычно работает немного быстрее, чем создание списка из генератора,
    # так как он оптимизирован для создания списков в памяти сразу.
    # Однако функция-генератор (process_list_gen) сама по себе (без list(...)) 
    # не хранит данные в памяти и работает "лениво", что критически важно 
    # при обработке очень больших массивов данных, где экономия памяти важнее 
    # незначительной разницы в скорости процессора.