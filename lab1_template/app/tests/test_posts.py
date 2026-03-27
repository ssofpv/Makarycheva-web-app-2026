import pytest

# 1. Тест главной страницы
def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

# 2. Тест страницы списка постов
def test_posts_index_status(client):
    response = client.get('/posts')
    assert response.status_code == 200
    assert "Последние посты" in response.text

# 3. Тест страницы конкретного поста
def test_post_detail_status(client):
    response = client.get('/posts/1')
    assert response.status_code == 200

# 4. Тест 404 ошибки (Требование задания)
def test_post_not_found(client):
    response = client.get('/posts/999')
    assert response.status_code == 404

# 5. Проверка заголовка поста в шаблоне
def test_post_content_title(client):
    response = client.get('/posts/1')
    assert "Заголовок поста" in response.text

# 6. Проверка имени автора
def test_post_content_author(client):
    response = client.get('/posts/1')
    assert "Toni Hernandez" in response.text

# 7. Проверка текста поста
def test_post_content_body(client):
    response = client.get('/posts/1')
    assert "Report first view" in response.text

# 8. Проверка правильного формата даты (Требование: dd.mm.yyyy)
def test_post_date_format(client):
    response = client.get('/posts/1')
    assert "22.08.2020" in response.text

# 9. Проверка наличия формы комментария
def test_comment_form_exists(client):
    response = client.get('/posts/1')
    assert '<textarea' in response.text
    assert 'Отправить' in response.text

# 10. Проверка наличия комментариев
def test_comments_presence(client):
    response = client.get('/posts/1')
    assert "Stephanie Franklin" in response.text

# 11. Проверка наличия ответов на комментарии
def test_replies_presence(client):
    response = client.get('/posts/1')
    assert "Andrew Mcconnell" in response.text

# 12. Проверка наличия изображения
def test_image_presence(client):
    response = client.get('/posts/1')
    assert 'post_image.jpg' in response.text

# 13. Проверка подвала (ФИО)
def test_footer_name(client):
    response = client.get('/posts')
    assert "Иванов Иван Иванович" in response.text

# 14. Проверка подвала (Группа)
def test_footer_group(client):
    response = client.get('/posts')
    assert "ИВТ-21-1" in response.text

# 15. Проверка страницы "Об авторе"
def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert "Об авторе" in response.text

# 16. Проверка тега <footer> в коде
def test_footer_tag_exists(client):
    response = client.get('/')
    assert '<footer' in response.text