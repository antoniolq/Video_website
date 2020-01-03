from . import home
from flask import render_template,redirect,url_for

@home.route("/")
def index():
    return render_template("/home/index.html")
    #return "<h1 style='color:green'> this is home </h1>"

@home.route("/login/")
def login():
    return render_template("/home/login.html")

@home.route("/logout/")
def logout():
    return redirect(url_for("/home.login"))

@home.route("/regist/")
def regist():
    return render_template("/home/regist.html")

@home.route("/user/")
def user():
    return render_template("/home/user.html")

@home.route("/pwd/")
def pwd():
    return render_template("/home/pwd.html")

@home.route("/comments/")
def comments():
    return render_template("/home/comments.html")

@home.route("/loginlog/")
def loginlog():
    return render_template("/home/loginlog.html")

@home.route("/animation/")
def animation():
    return render_template("/home/animation.html")

@home.route("/search/")
def search():
    return render_template("/home/search.html")

@home.route("/moviecol/")
def moviecol():
    return render_template("/home/moviecol.html")

@home.route("/play/")
def play():
    return render_template("/home/play.html")

@home.route("/movie/add/")
def movie_add():
    return render_template("/admin/movie_add.html")

@home.route("/movie/list/")
def movie_list():
    return render_template("/admin/movie_list.html")