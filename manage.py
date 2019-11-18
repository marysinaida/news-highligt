from app import create_app
from flask_script import Manager,Server

app = create_app()
manager = Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
    '''
    run the unittests.
    '''
    import unittest
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestResult(verbosity=2).run(tests)

if __name__ =='__main__':
    manager.run()