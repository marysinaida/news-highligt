import unittest
from app.models import News,Articles

class TestNews(unittest.TestCase):
    '''
    Test class to test the behaviour of our News class
    '''

    def setUp(self):
        '''
        Set up method that will run before ever Test
        '''
        self.new_news = News("abc-news","ABC News","Your trusted source for breaking news,analysis,exclusive interviews,headlines,and videos at ABCNews.com","https://abcnews.go.com","general","en","us")

    def setUp(self):