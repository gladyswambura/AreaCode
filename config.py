import os


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_FOLDER =os.environ.get('UPLOADED_FOLDER')

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:mock@localhost/areacode'
    DEBUG = True


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'testing': TestConfig
}
