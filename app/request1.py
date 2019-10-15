import urllib.request,json
from .models import News,Articles
from config import Config

article_base_url = Config.ARTICLE_API_BASE_URL


def get_news_home():
    '''
    Function that gets the json response to our url request
    '''

    with urllib.request.urlopen(article_base_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_result = None

        

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_result = process_news(news_results_list)


    return news_result

def process_news(news_list):
    news_result = []
    for source in news_list:
        title = source.get('title')
        author = source.get('author')
        description = source.get('description')
        url = source.get('url')
        urlToImage = source.get('urlToImage')
        publishedAt = source.get('publishedAt')
        
        if title:
            news_object = Articles(title,author,description,url,urlToImage,publishedAt)
            news_result.append(news_object)
    return news_result