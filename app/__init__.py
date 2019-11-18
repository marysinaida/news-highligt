from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

bootstrap =Bootstrap()

def create_app():
    app = Flask(__name__)

    #creating the app configurations
    app.config.from_object(Config)
    
    #Initializing flask extensions
    bootstrap.init_app(app)

    #Registration of the blue print
    from .requests import configure_request
    configure_request(app)

    #configuration setting
    from .requests import configure_request
    configure_request(app)

    return app



