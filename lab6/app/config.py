import os

SECRET_KEY = 'secret-key'

# Получаем абсолютный путь к папке instance
basedir = os.path.abspath(os.path.dirname(__file__))
instance_path = os.path.join(basedir, '..', 'instance')

SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(instance_path, "project.db")}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 
    '..',
    'media', 
    'images'
)