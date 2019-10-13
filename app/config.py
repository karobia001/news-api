class Config:
    '''
    General configuration parent class
    '''
    pass
NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&from=2019-09-13&sortBy=publishedAt&apiKey=03e8f078cdef4524ac7199eb9b6b12a1'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    