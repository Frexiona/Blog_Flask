from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# Secret would encrypt data
# import secrets
# secrets.token_hex(16)
app.config['SECRET_KEY'] = '37d901267ce7521740a16db50c4aa5a3'

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
