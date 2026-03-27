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