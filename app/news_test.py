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