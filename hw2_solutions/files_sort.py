import os
import sys

def sort_files(directory):
    if not os.path.exists(directory):
        print(f"Директория {directory} не найдена.")
        return

    try:
        # Получаем список всех элементов
        all_items = os.listdir(directory)
        
        # Фильтруем только файлы
        files = [f for f in all_items if os.path.isfile(os.path.join(directory, f))]
        
        # Сортировка: сначала по расширению, потом по имени
        # splitext возвращает (name, .ext), нам нужно сортировать по (ext, name)
        files.sort(key=lambda x: (os.path.splitext(x)[1], x))
        
        for f in files:
            print(f)
            
    except Exception as e:
        print(f"Ошибка при чтении директории: {e}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sort_files(sys.argv[1])
    else:
        print("Укажите путь к директории.")