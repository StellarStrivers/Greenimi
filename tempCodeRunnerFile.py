from flask import Flask, session, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user
from flask_session import Session
from flask import jsonify
import json


app = Flask(__name__)
app.config["SECRET_KEY"] = "AtigyiUS9812892024IKOSNJSGDU"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
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

with app.app_context():
    db.create_all()
    if not Quest.query.first():
        quests = [
            Quest(description="Recycle 5 plastic bottles", points=20),
            Quest(description="Walk instead of drive for a day", points=40),
            Quest(description="Shorten showers", points=30),
            Quest(description="Donate old clothes", points=35),
            Quest(description="Create different bins for different waste", points=50),
            Quest(description="Plant a tree", points=60),
            Quest(description="Donate old books", points=45),
            Quest(description="Hang a tote bag near doorway", points=50),
            Quest(description="Use Tote Bag 5 times", points=25),
            Quest(description="Buy a Bamboo Brush", points=30),
            Quest(description="Reuse Old Brushes for Cleaning", points=50),
            Quest(description="Install a Clothesline", points=60),
            Quest(description="Use Clothesline 10 times", points=35),
            Quest(description="Switch Study Room's LED light bulbs", points=50),
            Quest(description="Go Cycling when shopping this week", points=80),
            Quest(description="Learn about Composting", points=10),
            Quest(description="Install Composting Materials in House", points=50),
            Quest(description="Collect Food Waste", points=30),
            Quest(description="Compost 3 times", points=80),
            Quest(description="Buy Reusable Cutlery", points=70),
            Quest(description="Pack Reusable Cutlery in your go-to Bag", points=30),
            Quest(description="Use Reusable Cutlery for a week", points=50),
            Quest(description="Replace Tissues with Handkerchiefs", points=40),
            Quest(description="Next Time Shopping, try a thrift shop", points=50),
            Quest(description="Join a Sustainability event like Beach Cleaning", points=100)
            # Add more quests as needed
        ]
        db.session.add_all(quests)
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
    all_quests = Quest.query.filter_by(user_id=None).all()
    user_quests = Quest.query.filter_by(user_id=current_user.id).all()
    return render_template("tracker.html", points=points,all_quests=all_quests, user_quests=user_quests)

@app.route("/take_quest", methods=["POST"])
@login_required
def take_quest():
    quest_id = request.form.get("quest_id")
    quest = Quest.query.get(quest_id)
    if quest and quest.user_id is None:
        quest.user_id = current_user.id
        db.session.commit()
        return redirect(url_for('tracker'))
    return redirect(url_for('tracker', error="Quest already assigned"))


@app.route("/complete_quest", methods=["POST"])
@login_required
def complete_quest():
    quest_id = request.form.get("quest_id")
    quest = Quest.query.get(quest_id)
    if quest and quest.user_id == current_user.id:
        quest.user_id = None
        current_user.points += quest.points
        db.session.commit()
        return redirect(url_for('tracker'))

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
