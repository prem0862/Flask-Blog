from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationFrom, LoginFrom

app = Flask(__name__)
app.config['SECRET_KEY'] = '2a126bf2a1c20057adbf99aa967f99ca'

posts = [
    {
        'author': 'Prem Singh',
        'title': "Android Devlopement",
        'content': "I used to do android developement during my initial years",
        'date': '2020-09-13'
    },
    {
        'author': 'Prem Singh',
        'title': "Android Devlopement",
        'content': "I used to do android developement during my initial years",
        'date': '2020-09-13'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        if form.email.data == 'abc@gmail.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
        else:
            flash(f'Log in Unsuccessful. Please check your Email and Password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
