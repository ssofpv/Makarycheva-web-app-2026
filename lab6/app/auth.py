from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from .models import db, User
from .repositories import UserRepository

bp = Blueprint('auth', __name__)
user_repository = UserRepository(db)

@bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        remember = True if request.form.get('remember_me') else False
        
        user = user_repository.get_user_by_login(login)
        if user and user.check_password(password):
            login_user(user, remember=remember)
            flash('Вы успешно вошли в систему!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.index'))
        else:
            flash('Неверный логин или пароль.', 'danger')
    return render_template('auth/login.html')

@bp.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы.', 'info')
    return redirect(url_for('main.index'))