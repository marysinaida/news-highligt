from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

bootstrap = Bootstrap()

def create_app():

    app = Flask(__name__)

    #creating configurations of the app
    app.config.from_object(Config)

    #initializing flask extensions
    bootstrap.init_app(app)

    #Registratin of the blue print
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

   # setting config

    from .requests import configure_request
    configure_request(app)
   
   #addition of the views and forms

    return app