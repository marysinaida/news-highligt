import requests
from .models import News,Articles

#Getting api key
api_key = None

#Getting the news base url
base_url = None

def configure_request(app):
    '''
    Function that gets the json response to our url request
    '''
    global api_key,base_url,article_base_url
    api_key= app.config['NEWS_API_KEY']
    base_url =app.config['NEWS_API_BASE_URL']
    article_base_url = app.config['ARTICLE_API_BASE_URL']

def get_sources():
        '''
        Function that gets the json responce to our url request
        '''
        get_news_url = base_url + api_key

        get_news_response = request.get(get_news_url).json()

        if get_news_response['sources']:
                news_results_list = get_news_response['sources']
                news_results = process_results(news_results_list)
        return news_results
        
def process_results(news_results_list):
        news_results = []
        for news_items in news_results_list:
                id = news_item.get('id')
                name = news_item.get('name')
                description = news_item.get('description')
                url = news_item.get('url')
                category = news_list.get('category')
                language = news_list.get('language')
                country = news_list.get('country')
                if name:
                        news_obj = News(id,name,description,url,category,language,country)
                        news_list.append(news_obj)
                        return news_results      
#get article
def get_articles(id):
        get_articles_url = article_base.format(id,api_key)
        
        get_articles_response = request.get(get_articles_url).json()
        
        if get_articles_response['articles']:
                articles_results_list = get_articles_response['articles']
                articles_results = process_article(articles_results_list)
                
                return articles_results

def process_article(article_list):
        articles_results =[]
        for article in article_list:
                 id = article.get('id')
                 author = article.get('author')
                 title = article.get('title')
                 description = article.get('description')
                 url = article.get('url')
                 urlToImage = article.get('urlToImage')
                 publishedAt = article.get('publishedAt')
                 content = article.get('content')
                 if urlToImage:
                         article_result = Articles(id,author,title,description,url,urlToImage,publishedAt,content)
                         article_results.append(article_result)
        return articles_results

def search_news(name):
        search_news_url ='https://newsapi.org/v2/everything?q={}&apiKey={}'.format(name,api_key)
        search_news_response = requests.get(search_news_url).json()

        if search_news_response['articles']:
                search_news_list = search_news_response['articles']
                search_news_results = process_article(search_movie_list)
       
        return search_movie_results
 


        
        
            
  
     


