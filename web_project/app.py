from flask import Flask, render_template, request, url_for, redirect, jsonify
import sys
sys.path.append('../')
from analysis import director_genres, director_genres_popular

app = Flask(__name__)

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
    if type_ == 'director':
        director_genres.plotgraph(search.replace('+', ' ')) 
        director_genres_popular.plotgraph(search.replace('+', ' '))
    return render_template('show.html')

if __name__ == '__main__':
    app.run(debug=True)
