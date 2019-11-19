from .models import News,Articles
import requests

#Getting api key
api_key = None

#getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url,article_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_base_url = app.config['ARTICLE_API_BASE_URL']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format("f4b3c861a0db4b5b81c12a1477f9a7e7") 
    print(get_news_url)

    get_news_response = requests.get(get_news_url)
    news = get_news_response.json()
    get_news_response = news.get('sources')
    return get_news_response

    if get_news_response['sources']:
        news_results_list = get_news_response['sources']
        news_results = process_results(news_results_list)

        return news_results

def process_results(news_results_list):
    news_results = []
    for news_item in news_results_list:

        id= news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if name:
            news_obj = News(id, name, description,url,category,language,country)
            news_results.append(news_obj)
    return news_results


def get_articles(id):
    get_articles_url = article_base_url.format(id, "f4b3c861a0db4b5b81c12a1477f9a7e7")
    res = requests.get(get_articles_url)
    get_articles_response = res.json()
    article_list = get_articles_response.get('articles')
    return article_list


