from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles
from ..models import Sources, Articles

@main.route('/')
def index():
    '''
	view root page function that returns the index the page and its data
	'''
	# sources = get_sources()
    sources = get_sources('business')

    sports_sources = get_sources('sports')

    technology_sources = get_sources('technology')

    entertainment_sources = get_sources('entertainment')

    title = "News Hub"

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('.search',movie_name = search_movie))

    else: 

        return render_template('index.html',title = title,sources = sources, sports_sources = sports_sources, technology_sources = technology_sources, entertainment_sources = entertainment_sources)

@main.route('/sources/<id>')
def articles(id):
    '''
    view articles page
	'''

    articles = get_articles(id)
	
    title = "articles"

    return render_template('articles.html',title = title , articles = articles)

# @main.route('/source/<source>')
# def souce(source):
#     top_news = get_all_news(sources=source)

#     title = source.title()

#     return render_template("source.html", news_articles=top_news, title=title, source=title)        