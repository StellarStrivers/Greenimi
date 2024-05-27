from flask import Flask, session, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user
from flask_session import Session


app = Flask(__name__)
app.config["SECRET_KEY"] = "AtigyiUS9812892024IKOSNJSGDU"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.init_app(app)


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(40), nullable=False)
    points = db.Column(db.Integer,nullable=False)

db.init_app(app)
with app.app_context():
    db.create_all()


@login_manager.user_loader
def user_load(user_id):
    return Users.query.get(user_id)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/home")
def homes():
    return render_template("home_loggedin.html")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(email=request.form.get("email")).first()
        if user.password == request.form.get("password"):
            login_user(user)
            session["user"] = user
            session["user"]= user.points
            logins= True
            return render_template("home_loggedin.html", login=logins, points= user.points)
    return render_template("login.html")

@app.route("/shop")
def shop():
    user = session.get("user")
    points = user.points if user else 0
    return render_template("monshop.html", points=points)

@app.route("/tracker")
def tracker():
    user = session.get("user")
    points = user.points if user else 0
    return render_template("tracker.html", points=points)


@app.route('/logout')
def logout():
    # Simulating a logout
    session.pop('username', None)
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        points = 100
        user = Users(name=name, email=email, username=username, password=password, points=points)
        db.session.add(user)
        db.session.commit()
        return render_template("home_loggedin.html")
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug="True")
