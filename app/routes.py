from flask import render_template
from app import app

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
