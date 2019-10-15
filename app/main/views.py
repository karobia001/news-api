from flask import render_template
from . import main
from app.request import get_sources
from app.request1 import get_news_home

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    popular_news = get_news_home()
    name = 'Home - Welcome to Trending news'
    return render_template('index.html', name=name,popular_news = popular_news)
  
@main.route('/news')
def news():

    '''
    View news page function that returns the news details page and its data
    '''
    sources = get_sources()
    return render_template('articles.html', sources=sources)