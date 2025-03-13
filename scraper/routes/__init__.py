from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    from scraper.routes.home import bp
    app.register_blueprint(bp)
    
    return app

