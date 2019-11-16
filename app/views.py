from flask import render_template
from app import app

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page fuction that returns the movie details page and its data
    '''
    return render_template('news.html',id = news_id)

#Views
@app.route('/')
def index():

    '''
    Views root page function that returns the index page and its data
    '''
    message = 'Welcome to News Highlights'
    return render_template('index.html',message = message)
