from distutils.debug import DEBUG
import os

from flask_uploads import configure_uploads

class Config():
    pass

class DevConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'testing': TestConfig
}