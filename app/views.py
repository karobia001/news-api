from flask import render_template
from app import app
from .request import get_news_home,get_news,get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # message = 'Hello world'
    # return render_template('index.html',message = message)
    
    
  # Getting po  # Getting popular news
    popular_news = get_news_home()
    print(popular_news)
    name = 'Home - Welcome to Trending news'
    print(popular_news)
    return render_template('index.html', name=name,popular = popular_news)
  
@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    articles = get_articles(news_id)
    return render_template('articles.html', articles=articles)