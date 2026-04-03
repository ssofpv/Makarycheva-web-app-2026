<<<<<<< HEAD
import random
from functools import lru_cache
from flask import Flask, render_template, abort  # Добавлен abort
from faker import Faker

fake = Faker()

app = Flask(__name__)
application = app

images_ids = ['7d4e9175-95ea-4c5f-8be5-92a6b708bb3c',
              '2d2ab7df-cdbc-48a8-a936-35bba702def5',
              '6e12f3de-d5fd-4ebb-855b-8cbc485278b7',
              'afc2cfe7-5cac-4b80-9b9a-d5c65ef0c728',
              'cab5b7f2-774e-4884-a200-0c0180fa777f']

def generate_comments(replies=True):
    comments = []
    for _ in range(random.randint(1, 3)):
        comment = { 'author': fake.name(), 'text': fake.text() }
        if replies:
            comment['replies'] = generate_comments(replies=False)
        comments.append(comment)
    return comments

def generate_post(i):
    return {
        'title': f'Заголовок поста {i+1}',
        'text': fake.paragraph(nb_sentences=100),
        'author': fake.name(),
        'date': fake.date_time_between(start_date='-2y', end_date='now'),
        'image_id': f'{images_ids[i]}.jpg',
        'comments': generate_comments()
    }

@lru_cache
def posts_list():
    return sorted([generate_post(i) for i in range(5)], key=lambda p: p['date'], reverse=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', title='Посты', posts=posts_list())

@app.route('/posts/<int:index>')
def post(index):
    # Логика для обработки 404 ошибки
    all_posts = posts_list()
    if index < 0 or index >= len(all_posts):
        abort(404)
    p = all_posts[index]
    return render_template('post.html', title=p['title'], post=p)

@app.route('/about')
def about():
    return render_template('about.html', title='Об авторе')
=======
from flask import Flask, render_template, abort
from datetime import datetime

app = Flask(__name__)

# Имитация базы данных
posts_list = [
    {
        "id": 1,
        "title": "Заголовок поста",
        "author": "Toni Hernandez",
        "date": datetime(2020, 8, 22),
        "image": "post_image.jpg",
        "text": "Report first view. Wide research already difficult he point weight. Whatever food shoulder quite beat investment. Job behind way build prove both through quickly. Fund whether challenge entire no. Trouble somebody seat center cultural someone. Environmental many nature prove heavy.",
        "comments": [
            {
                "author": "Stephanie Franklin",
                "text": "Leave whom discussion possible win. Performance Democrat fund that short hit song.",
                "replies": [
                    {
                        "author": "Andrew Mcconnell",
                        "text": "Data now less religious. Action argue surface memory decision."
                    }
                ]
            }
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', title='Главная')

@app.route('/posts')
def posts():
    return render_template('posts.html', title='Посты', posts=posts_list)

@app.route('/posts/<int:post_id>')
def post_detail(post_id):
    # Ищем пост по ID
    post = next((p for p in posts_list if p['id'] == post_id), None)
    if post is None:
        abort(404)
    return render_template('post.html', title=post['title'], post=post)

@app.route('/about')
def about():
    return render_template('about.html', title='Об авторе')

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> e4ecf103fabf75370ed57082727088c4086b4bda
