import os

class Config:
    '''
    Parent class
    '''

    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&apiKey={}'
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True

class ProdConfig(Config):
    '''
    Production class
    '''
    pass

class DevConfig(Config):
    '''
    Development class
    '''

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}