import sys
import os
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import Flask

# Добавляем все папки с лабораторными в путь Python
current_dir = os.path.dirname(os.path.abspath(__file__))

# Добавляем корневую папку
sys.path.insert(0, current_dir)

# Добавляем каждую лабораторную отдельно
for lab in ['lab1', 'lab2', 'lab3', 'lab4', 'lab5', 'lab6']:
    lab_path = os.path.join(current_dir, lab)
    if os.path.exists(lab_path):
        sys.path.insert(0, lab_path)
        
# Для lab1 нужен путь к подпапке app
lab1_app_path = os.path.join(current_dir, 'lab1', 'app')
if os.path.exists(lab1_app_path):
    sys.path.insert(0, lab1_app_path)

# Создаем главное приложение Flask
main_app = Flask(__name__)

@main_app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Все лабораторные работы</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            .header {
                background: rgba(255,255,255,0.95);
                border-radius: 20px;
                margin-top: 50px;
                padding: 30px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            }
            h1 {
                color: #333;
                font-weight: 700;
                margin-bottom: 10px;
            }
            .subtitle {
                color: #666;
                margin-bottom: 30px;
            }
            .lab-card {
                background: white;
                border-radius: 15px;
                padding: 25px;
                margin-bottom: 20px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                cursor: pointer;
                text-decoration: none;
                display: block;
                color: inherit;
            }
            .lab-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 15px 40px rgba(0,0,0,0.2);
                text-decoration: none;
                color: inherit;
            }
            .lab-number {
                font-size: 2.5rem;
                font-weight: bold;
                color: #667eea;
                margin-bottom: 10px;
            }
            .lab-title {
                font-size: 1.3rem;
                font-weight: 600;
                margin-bottom: 10px;
            }
            .lab-desc {
                color: #777;
                font-size: 0.9rem;
            }
            .footer {
                text-align: center;
                padding: 20px;
                color: white;
                margin-top: 30px;
            }
            .badge-lab {
                position: absolute;
                top: 20px;
                right: 20px;
                background: #667eea;
                color: white;
                padding: 5px 12px;
                border-radius: 20px;
                font-size: 0.8rem;
            }
            .lab-card {
                position: relative;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header text-center">
                <h1>📚 Все лабораторные работы</h1>
                <p class="subtitle">Веб-приложение на Flask | Московский Политех</p>
                <p class="subtitle">Макарычева Софья Альбертовна | Группа 241-371</p>
            </div>

            <div class="row mt-4">
                <div class="col-md-6">
                    <a href="/lab1/" class="lab-card">
                        <div class="lab-number">Лабораторная работа №1</div>
                        <div class="lab-title">📝 Flask-приложение с постами</div>
                        <div class="lab-desc">Шаблонизация, генерация постов, комментарии</div>
                    </a>
                </div>
                <div class="col-md-6">
                    <a href="/lab2/" class="lab-card">
                        <div class="lab-number">Лабораторная работа №2</div>
                        <div class="lab-title">🔍 Параметры запроса и валидация</div>
                        <div class="lab-desc">URL params, headers, cookies, валидация телефона</div>
                    </a>
                </div>
                <div class="col-md-6">
                    <a href="/lab3/" class="lab-card">
                        <div class="lab-number">Лабораторная работа №3</div>
                        <div class="lab-title">🔐 Аутентификация</div>
                        <div class="lab-desc">Flask-Login, счётчик посещений, сессии</div>
                    </a>
                </div>
                <div class="col-md-6">
                    <a href="/lab4/" class="lab-card">
                        <div class="lab-number">Лабораторная работа №4</div>
                        <div class="lab-title">👥 CRUD пользователей</div>
                        <div class="lab-desc">Создание, редактирование, удаление, роли</div>
                    </a>
                </div>
                <div class="col-md-6">
                    <a href="/lab5/" class="lab-card">
                        <div class="lab-number">Лабораторная работа №5</div>
                        <div class="lab-title">📊 Журнал посещений и отчёты</div>
                        <div class="lab-desc">Статистика, CSV-экспорт, права доступа</div>
                    </a>
                </div>
                <div class="col-md-6">
                    <a href="/lab6/" class="lab-card">
                        <div class="lab-number">Лабораторная работа №6</div>
                        <div class="lab-title">⭐ Отзывы к курсам</div>
                        <div class="lab-desc">Рейтинг, комментарии, пагинация, сортировка</div>
                    </a>
                </div>
            </div>

            <div class="footer">
                <p>© 2026 | Все лабораторные работы выполнены в рамках дисциплины "Веб-программирование"</p>
            </div>
        </div>
    </body>
    </html>
    '''

# Импортируем ваши приложения
try:
    from lab1.app.app import app as lab1_app
    print('✓ lab1 загружена')
except ImportError as e:
    print(f'✗ Ошибка загрузки lab1: {e}')
    lab1_app = Flask(__name__)
    @lab1_app.route('/')
    def lab1_error(): return "Лабораторная работа №1 не загружена", 500

try:
    from lab2.app import app as lab2_app
    print('✓ lab2 загружена')
except ImportError as e:
    print(f'✗ Ошибка загрузки lab2: {e}')
    lab2_app = Flask(__name__)
    @lab2_app.route('/')
    def lab2_error(): return "Лабораторная работа №2 не загружена", 500

try:
    from lab3.app import app as lab3_app
    print('✓ lab3 загружена')
except ImportError as e:
    print(f'✗ Ошибка загрузки lab3: {e}')
    lab3_app = Flask(__name__)
    @lab3_app.route('/')
    def lab3_error(): return "Лабораторная работа №3 не загружена", 500

try:
    from lab4.app import app as lab4_app
    print('✓ lab4 загружена')
except ImportError as e:
    print(f'✗ Ошибка загрузки lab4: {e}')
    lab4_app = Flask(__name__)
    @lab4_app.route('/')
    def lab4_error(): return "Лабораторная работа №4 не загружена", 500

try:
    from lab5.app import app as lab5_app
    print('✓ lab5 загружена')
except ImportError as e:
    print(f'✗ Ошибка загрузки lab5: {e}')
    lab5_app = Flask(__name__)
    @lab5_app.route('/')
    def lab5_error(): return "Лабораторная работа №5 не загружена", 500

# Импорт ЛР6 (через фабрику приложений, с правильным путём)
try:
    # Добавляем путь к папке lab6
    lab6_path = os.path.join(current_dir, 'lab6')
    sys.path.insert(0, lab6_path)
    
    # Импортируем из папки app
    from app import create_app
    lab6_app = create_app()
    print('✓ lab6 загружена')
except ImportError as e:
    print(f'✗ Ошибка загрузки lab6: {e}')
    lab6_app = Flask(__name__)
    @lab6_app.route('/')
    def lab6_error(): return f"Лабораторная работа №6 не загружена: {e}", 500

# Создаем WSGI-приложение, которое будет направлять запросы
application = DispatcherMiddleware(main_app, {
    '/lab1': lab1_app,
    '/lab2': lab2_app,
    '/lab3': lab3_app,
    '/lab4': lab4_app,
    '/lab5': lab5_app,
    '/lab6': lab6_app,   # Префикс добавляется здесь
})

if __name__ == '__main__':
    run_simple('127.0.0.1', 5000, application, use_debugger=True, use_reloader=True)