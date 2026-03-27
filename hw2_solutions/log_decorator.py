import datetime
import time
from functools import wraps

def function_logger(file_path):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            start_ts = time.time()
            
            result = None
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                end_time = datetime.datetime.now()
                end_ts = time.time()
                duration = end_ts - start_ts
                
                log_entry = [
                    f"{func.__name__}",
                    f"{start_time.strftime('%Y-%m-%d %H:%M:%S.%f')}",
                    f"{args if args else ''}",
                    f"{kwargs if kwargs else ''}", # Дополнительно добавил kwargs для полноты
                    f"{result if result is not None else '-'}",
                    f"{end_time.strftime('%Y-%m-%d %H:%M:%S.%f')}",
                    f"{datetime.timedelta(seconds=duration)}" # формат 0:00:00.000003
                ]
                
                # Убираем пустые строки, если args/kwargs пустые (чтобы соответствовать примеру)
                # В примере вывод args: ('John',), но если args пуст, пример не показывает вывод.
                # Подгоним под пример:
                lines = []
                lines.append(func.__name__)
                lines.append(start_time.strftime('%Y-%m-%d %H:%M:%S.%f'))
                if args:
                    lines.append(str(args))
                if kwargs:
                    lines.append(str(kwargs))
                
                # Пример вывода результата: Hello, John! (без кавычек кортежа)
                lines.append(str(result) if result is not None else '-')
                
                lines.append(end_time.strftime('%Y-%m-%d %H:%M:%S.%f'))
                lines.append(str(datetime.timedelta(seconds=duration)))
                
                with open(file_path, 'a', encoding='utf-8') as f:
                    f.write('\n'.join(lines) + '\n\n')
                    
        return wrapper
    return decorator

if __name__ == '__main__':
    @function_logger('test.log')
    def greeting_format(name):
        return f'Hello, {name}!'

    greeting_format('John')