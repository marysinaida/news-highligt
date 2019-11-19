import os

class Config:
    '''
    general configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True

class prodConfig(Config):
    '''
    production configurations child class
    Args:
       Config:The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
       Config: The parent configuration class with general configuration settings
    '''

config_options = {
    'development':DevConfig,
    'production':prodConfig
}
       
    



