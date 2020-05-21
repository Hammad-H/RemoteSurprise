from flask import render_template, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Hammad'}
    recommendations = [
        {
            'friend': {'username' : 'Mahad'},
            'title': 'Two and a Half Men',
            'type': 'Series'
        },
        {
            'friend': {'username': 'Salar'},
            'title': 'The Imitation Game',
            'type': 'Movie'
        }
    ]

    return render_template('index.html', title = 'Home', user = user, recommendations = recommendations)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
        form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign In', form = form)
