from flask import Flask, session, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user
from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = "AtigyiUS9812892024IKOSNJSGDU"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(40), nullable=False)
    points = db.Column(db.Integer,nullable=False)

class PetMon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    rank = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(100), nullable=False)  # URL or path to the image

db.init_app(app)
with app.app_context():
    db.create_all()

with app.app_context():
    db.create_all()
    # Add initial pet monsters if not already added
    if not PetMon.query.first():
        mons = [
            PetMon(name="Lady Flipperton", rank="Common", points=160, image="seal-grey.jpg"),
            PetMon(name="Young Mater Hugguin", rank="Common", points=180, image="cutepenguin.jpg"),
            PetMon(name="Lady Penguinella", rank="Common", points=150, image="penguin-heart.jpg"),
            PetMon(name="Captain Stripes", rank="Rare", points=300, image="tiger_baby.jpg"),
            PetMon(name="Lord Whiskers", rank="Rare", points=450, image="magic_cat.jpg"),
            PetMon(name="Knight Axolart", rank="Rare", points=250, image="pinkaxolot.jpg"),
            PetMon(name="Princess Vinefox", rank="Epic", points=600, image="floralfox.jpg"),
            PetMon(name="Dame Caulilou", rank="Epic", points=500, image="cauliflower.jpg"),
            PetMon(name="Lady Springbell", rank="Legendary", points=800, image="bluefox.jpg"),
            PetMon(name="Mr. Raborrot", rank="Legendary", points=770, image="carrot_rabbit.jpg"),
            PetMon(name="Duke Foxclo", rank="Legendary", points=890, image="wingfox.jpg"),
            PetMon(name="Baron Bathart", rank="Extinct", points=1200, image="zoobat.jpg"),
            PetMon(name="Queen Horsesea", rank="Extinct", points=2000, image="waterpony.jpg"),
            PetMon(name="Duke Dandeleon", rank="Extinct", points=1600, image="dandelionlion.jpg")
            
            # Add more pet monsters as needed
        ]
        db.session.add_all(mons)
        db.session.commit()

@login_manager.user_loader
def user_load(user_id):
    return Users.query.get(int(user_id))

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
            session["user_id"] = user.id
            session["user"]= user.points
            logins= True
            return render_template("home_loggedin.html", login=logins, points= user.points)
    return render_template("login.html")

@app.route("/shop")
@login_required
def shop():
    points = current_user.points
    mons = PetMon.query.all()
    return render_template("monshop.html", points=points, mons=mons)

@app.route("/buy_mon", methods=["POST"])
@login_required
def buy_mon():
    mon_id = request.form.get("mon_id")
    mon = PetMon.query.get(mon_id)
    if mon and current_user.points >= mon.points:
        current_user.points -= mon.points
        db.session.commit()
        # You can add logic to save the purchase if needed
        return redirect(url_for('shop'))
    return redirect(url_for('shop', error="Not enough points or invalid monster"))


@app.route("/tracker")
@login_required
def tracker():
    points = current_user.points
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
        user = Users(name=name, email=email, username=username, password=password,
points=points)
        db.session.add(user)
        db.session.commit()
        return render_template("home_loggedin.html")
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug="True")

