"""Flask configuration."""
from os import environ, path



class Config:
    """Base config."""
    pass
    # STATIC_FOLDER = 'static'
    # TEMPLATES_FOLDER = 'templates'


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'mongodb+srv://root:root@esibase.pvzqm3r.mongodb.net/?retryWrites=true&w=majority'



class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'mongodb://10.10.10.57:27017/'

class testConfig(Config):
    FLASK_ENV = 'test'
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'mongodb://localhost:27017/'
