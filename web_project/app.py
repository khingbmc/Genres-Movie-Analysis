from flask import Flask, render_template, request, url_for, redirect, jsonify
import sys
sys.path.append('../')
from analysis import director_genres, director_genres_popular, genres_popularity, production_genres_popular, production_genres_analytic
import random

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.cache_control.max_age = 0
    return response

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/credit')
def credit():
    return render_template('credit.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/show', methods=['GET'])
def show():
    search = request.args.get('search', None)
    type_ = request.args.get('type_', None)
    if type_ == 'years':
        genres_popularity.plotgraph(search, 0)
        return render_template('show_year.html')
    elif type_ == 'director':
        director_genres.plotgraph(search.replace('+', ' ')) 
        director_genres_popular.plotgraph(search.replace('+', ' '))
        return render_template('show_director.html', a='random.random()*100', c='random.random()*100', b='type_')
    else:
        production_genres_analytic.plotgraph(search.replace('+', ' '))
        production_genres_popular.plotgraph(search.replace('+', ' '))
        return render_template('show_production.html', a='random.random()*100', c='random.random()*100', b='type_')

if __name__ == '__main__':
    app.run(debug=True)
