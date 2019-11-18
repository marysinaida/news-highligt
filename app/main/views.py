from flask import render_template
from .import main
from ..requests import get_sources, get_articles, search_news

@main.route('/')
def index():
    '''
    View news page fuction that returns the movie details page and its data
    '''
    #getting news source
    news_source = get_sources()

    title = 'Home - welcome to The best News Highlights Website Online'
    search_new = request.args.get('news_query')
    return render_template('index.html', title = title,news_source = news_source)

#Views
@main.route('/news/<id>')
def news(id):
    #getting article

    '''
    Views root page function that returns the index page and its data
    '''
    article = get_articles(id)
    print(article)
    return render_template('article.html',article = article)

@main.route('/search/<name>')
def search(name):
    '''
    A view function that displays the search results
    '''
    news_name_list = name.split("")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {name}'
    return render_template('search.html', news = searched_news, title = title)
