from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles,search_news

#views
@main.route('/')
def index():

    '''
    view root page function that returns the index page and its data
    '''

    #Getting news sources
    news_source = get_sources()

    title = 'Home - Welcome to The best News Highlight Website Online'
    search_news = request.args.get('news_query')
    if search_news:
        return redirect(url_for('main.search',name = search_news))
    else:
        return render_template('index.html',title = title,news_source = news_source)

@main.route('/news/<id>')
def news(id):
    article = get_articles(id)
    print(article)
    return render_template('article.html',article = article)

@main.route('/search/<name>')
def search(name):
    '''
    view function to display the search results
    '''

    news_name_list = name.split("")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {name}'
    return render_template('search.html',news = searched_news,title = title)