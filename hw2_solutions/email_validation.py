import re

def fun(s):
    # Regex:
    # ^ - начало строки
    # [a-zA-Z0-9_-]+ - имя пользователя (буквы, цифры, _, -)
    # @ - символ @
    # [a-zA-Z0-9]+ - сайт (буквы, цифры)
    # \. - точка
    # [a-zA-Z]{1,3} - расширение (только буквы, длина 1-3)
    # $ - конец строки
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, s))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    try:
        n = int(input())
        emails = []
        for _ in range(n):
            emails.append(input())

        filtered_emails = filter_mail(emails)
        filtered_emails.sort()
        print(filtered_emails)
    except (ValueError, EOFError):
        pass