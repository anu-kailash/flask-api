from myapp import app
from model import Album
from forms import LoginForm
from flask import render_template
from test import session


@app.route('/')
def index():
    title = session.query(Album).get(2)
    return '<h1>The title is:' + title.Title + '</h1>'


@app.route('/login')
def login():
    form= LoginForm()
    return render_template('index.html', form=form)

