from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# Secret would encrypt data
# import secrets
# secrets.token_hex(16)
app.config['SECRET_KEY'] = '37d901267ce7521740a16db50c4aa5a3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # Pass the functions but not current time
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


posts = [
    {
        'author': 'Rex',
        'title': 'Firstshot',
        'content': 'Firstshot',
        'date': '11-11-2019'
    },
    {
        'author': 'Fiona',
        'title': 'Secondshot',
        'content': 'Secondshot',
        'date': '12-12-2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='ABOUT')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Alerts
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
