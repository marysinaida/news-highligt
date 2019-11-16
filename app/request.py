from app import app
import urllib.request,json
from .models import News,Articles

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(source):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_news_url)as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_movies_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

    return news_results
def process_results(news_list):
    '''
     Function  that processes the news result and transform them to a list of Objects
     
     Args:
      news_list:A list of news objects
    '''
    news_results =[]
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_list.get('category')
        language = news_list.get('language')
        country = news_list.get('country')

        if name:
            news-obj = News(id,name,description,url,category,language,country)
            news_list.append(news_obj)
    return news_results        
#get article



