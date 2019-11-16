from flask import render_template
from app import app

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page fuction that returns the movie details page and its data
    '''
    title = f'You are viewing {news_id}'
    return render_template('news.html',title = title)

#Views
@app.route('/')
def index():

    '''
    Views root page function that returns the index page and its data
    '''
    title = 'Home - welcome to The best News Highlights Website Online'
    return render_template('index.html',title = title)
