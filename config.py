# config.py

class Config(object):
    """
    Common configurations
    """
    
class DevelopmentConfig(Config):
    """
    Development configurations
    """

    TESTING = True
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """
    
    TESTING = False
    DEBUG = False



app_config = {
    
        'development': DevelopmentConfig,
        'production': ProductionConfig
}
