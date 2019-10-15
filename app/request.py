
import urllib.request,json
from .models import News,Articles
from config import Config




# # Getting api key
# api_key = Config.NEWS_API_KEY

#Getting the news base url

base_url = Config.NEWS_API_BASE_URL
article_base_url = Config.ARTICLE_API_BASE_URL


    
    

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    # get_articles_url = article_base_url.format(category)

    with urllib.request.urlopen(base_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        news_results = None

        if get_articles_response['sources']:
            articles_articles_list = get_articles_response['sources']
            print(articles_articles_list)
            news_results = process_articles(articles_articles_list)


    return news_results


def process_articles(news_list):
    '''
    Function  that processes the  news result and transform them to a list of Objects

    Args:
        sources: A list of dictionaries that contain movie details

    Returns :
         sources results: A list of movie objects
    '''
    news_results = []
    
    for news_item in news_list:
        id =news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url =  news_item.get('url')
        category= news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')
        if language == 'en':
            news_results.append(News(id, name, description, url, category, language, country))
        
    return news_results


# def get_articles1(id):
#     get_articles_details_url = base_url.format(id,api_key)

#     with urllib.request.urlopen(get_articles_details_url) as url:
#         articles_details_data = url.read()
#         articles_details_response = json.loads(articles_details_data)

#         articles_object = None
#         if articles_details_response:
#             author = articles_details_response.get('author')
#             title = articles_details_response.get('title')
#             description = articles_details_response.get('description')
#             url = articles_details_response.get('url')
#             urlToImage = articles_details_response.get('urlToImage')
#             publishedAt = articles_details_response.get('publishedAt')

#             articles_object = Articles(id,author,title,url,urlToImage,publishedAt,content)

#     return articles_object
