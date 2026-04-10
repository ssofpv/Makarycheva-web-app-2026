from flask import Flask
from flask_migrate import Migrate
from sqlalchemy.exc import SQLAlchemyError
from flask_login import LoginManager

from .models import db
from .auth import bp as auth_bp
from .courses import bp as courses_bp
from .routes import bp as main_bp

def handle_sqlalchemy_error(err):
    error_msg = ('Возникла ошибка при подключении к базе данных. '
                 'Повторите попытку позже.')
    return f'{error_msg} (Подробнее: {err})', 500

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False, static_url_path='/lab6/static')
    app.config.from_pyfile('config.py')

    if test_config:
        app.config.from_mapping(test_config)

    db.init_app(app)
    migrate = Migrate(app, db)

    # Настройка LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Пожалуйста, войдите для доступа к этой странице.'
    
    from .repositories import UserRepository
    user_repository = UserRepository(db)
    
    @login_manager.user_loader
    def load_user(user_id):
        return user_repository.get_user_by_id(user_id)

    # Регистрация Blueprint без префиксов (префикс будет добавлен в main_app.py)
    app.register_blueprint(auth_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(main_bp)
    app.errorhandler(SQLAlchemyError)(handle_sqlalchemy_error)

    return app