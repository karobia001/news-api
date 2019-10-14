from app import app
import urllib.request,json
from .models import news,articles

News = news.News
Articles = articles.Articles


# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url

base_url = app.config["NEWS_API_BASE_URL"]
article_base_url = app.config["ARTICLE_API_BASE_URL"]


def get_news_home():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url
    
    news_results = None

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_news(news_results_list)


    return news_results

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = article_base_url.format(category)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        news_results = None

        if get_articles_response['articles']:
            articles_articles_list = get_articles_response['articles']
            print(articles_articles_list)
            news_results = process_articles(articles_articles_list)


    return news_results


def process_news(news_list):
    '''
    Function  that processes the  news result and transform them to a list of Objects

    Args:
        sources: A list of dictionaries that contain movie details

    Returns :
         sources results: A list of movie objects
    '''
    news_results = []
    
    for news_item in news_list:
        print(news_item)
        id =news_item.get('id')
        names = news_item.get('name')
        description = news_item.get('description')
        url =  news_item.get('url')
        category= news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')
        
        news_results.append(News(id, names, description, url, category, language, country))
        
    return news_results

def process_articles(articles_list):
    '''
    Function  that processes the  news result and transform them to a list of Objects

    Args:
        sources: A list of dictionaries that contain movie details

    Returns :
         sources results: A list of movie objects
    '''
    articles_results = []
    for articles_item in articles_list:
        #source =articles_item.get('source')
        author = articles_item.get('author')
        title = articles_item.get('title')
        description  =  articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content') 
        
        
        articles_results.append(Articles("",author,title,description,url,urlToImage,publishedAt,content))
        #  if poster:
        #     news_object = News(id,names,description,url,category,language,country)
        #     news_results.append(news_object)
    return articles_results

# getting movie setails

def get_news(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            names = news_details_response.get('name')
            description = news_details_response.get('description')
            url = news_details_response.get('url')
            category = news_details_response.get('category')
            language = news_details_response.get('language')
            country = news_details_response.get('country')

            news_object = News(id,names,description,url,category,language,country)

    return news_object

def get_articles1(id):
    get_articles_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_object = None
        if articles_details_response:
            source = articles_details_response.get('id')
            author = articles_details_response.get('author')
            title = articles_details_response.get('title')
            description = articles_details_response.get('description')
            url = articles_details_response.get('url')
            urlToImage = articles_details_response.get('urlToImage')
            publishedAt = articles_details_response.get('publishedAt')
            content = articles_details_response.get('content')

            articles_object = Articles(id,author,title,url,urlToImage,publishedAt,content)

    return articles_object
