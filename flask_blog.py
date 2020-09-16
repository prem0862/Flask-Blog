from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
