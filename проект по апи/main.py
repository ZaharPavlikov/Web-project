from flask import Flask, render_template, request
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data import db_session
from data.news import News
from data.buy import Buy
from data.man_clother import ManClotherA
from data.users import User
import os
import shutil
from PIL import Image
import secrets
from werkzeug.utils import secure_filename
from forms.news import NewsForm
from forms.buy import BuysForm
from forms.man_clother import ManClother
from forms.user import RegisterForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/man_clother')
def man_clother():
    db_sess = db_session.create_session()
    # news = db_sess.query(News).filter(News.is_private != True)
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("man_clother.html", news=news)

@app.route('/man_clother/futbolki')
def futbolki():
    db_sess = db_session.create_session()
    # news = db_sess.query(News).filter(News.is_private != True)
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("fut_m.html", news=news)

@app.route('/man_clother/shtani')
def shtani():
    db_sess = db_session.create_session()
    # news = db_sess.query(News).filter(News.is_private != True)
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("shtan_m.html", news=news)

@app.route('/man_clother/kofti')
def kofti():
    db_sess = db_session.create_session()
    # news = db_sess.query(News).filter(News.is_private != True)
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("kof_m.html", news=news)

@app.route('/man_clother/shorti')
def shorti():
    db_sess = db_session.create_session()
    # news = db_sess.query(News).filter(News.is_private != True)
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("short_m.html", news=news)


@app.route('/woman_clother')
def woman_clother():
    db_sess = db_session.create_session()
    # news = db_sess.query(News).filter(News.is_private != True)
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("woman_clother.html", news=news)

@app.route('/woman_clother/futbolki')
def w_futbolki():
    db_sess = db_session.create_session()
    # news = db_sess.query(News).filter(News.is_private != True)
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("fut_w.html", news=news)

@app.route('/woman_clother/shtani')
def w_shtani():
    db_sess = db_session.create_session()
    # news = db_sess.query(News).filter(News.is_private != True)
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("shtan_w.html", news=news)

@app.route('/woman_clother/kofti')
def w_kofti():
    db_sess = db_session.create_session()
    # news = db_sess.query(News).filter(News.is_private != True)
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("kof_w.html", news=news)

@app.route('/woman_clother/shorti')
def w_shorti():
    db_sess = db_session.create_session()
    # news = db_sess.query(News).filter(News.is_private != True)
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("short_w.html", news=news)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    # news = db_sess.query(News).filter(News.is_private != True)
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)

@app.route("/buy_history")
@login_required
def buy_history():
    db_sess = db_session.create_session()
    # news = db_sess.query(News).filter(News.is_private != True)
    if current_user.is_authenticated:
        buy = db_sess.query(Buy).filter((Buy.user == current_user))
    else:
        buy = db_sess.query(Buy).filter()
    return render_template("history.html", buy=buy)


@app.route('/news', methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        f = form.image.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.instance_path, 'static', 'img', filename))
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.pol = form.pol.data
        news.content = form.content.data
        news.types = form.language.data
        news.is_private = form.is_private.data
        news.image_file = filename
        current_user.news.append(news)
        db_sess.merge(current_user)
        db_sess.commit()
        file_source = 'C:/Users/User/Desktop/ЯЛицей/проект по апи/instance/static/img/'
        file_destination = 'C:/Users/User/Desktop/ЯЛицей/проект по апи/static/'
 
        get_files = os.listdir(file_source)
 
        for g in get_files:
            os.replace(file_source + g, file_destination + g)
        return redirect('/')
    return render_template('news.html', title='Добавление товара',
                           form=form)


@app.route('/buy_clother', methods=['GET', 'POST'])
@login_required
def buy_clother():
    form = BuysForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        buy = Buy()
        buy.title = form.title.data
        buy.address = form.content.data
        buy.size = form.language.data
        current_user.buy.append(buy)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('buy.html', title='Оформление заказа',
                           form=form)


@app.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = NewsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user
                                          ).first()
        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user
                                          ).first()
        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('news.html',
                           title='Редактирование новости',
                           form=form
                           )


@app.route('/news_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id,
                                      News.user == current_user
                                      ).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
