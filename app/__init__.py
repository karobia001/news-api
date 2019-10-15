from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    
    # Initializing application
    app = Flask(__name__,instance_relative_config = True)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    
    #initialising blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Initializing Flask Extensions
    bootstrap.init_app
    
    return app


