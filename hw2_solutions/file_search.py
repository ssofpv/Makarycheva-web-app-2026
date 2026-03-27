import os
import sys

def search_file(filename, search_path="."):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    print(f"--- Файл найден: {file_path} ---")
                    for _ in range(5):
                        line = f.readline()
                        if not line:
                            break
                        print(line.rstrip())
                return True
            except Exception as e:
                print(f"Ошибка при чтении файла: {e}")
                return True # Файл найден, но не прочитан
    
    print(f"Файл {filename} не найден")
    return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
        search_file(target_file)
    else:
        print("Укажите имя файла для поиска.")