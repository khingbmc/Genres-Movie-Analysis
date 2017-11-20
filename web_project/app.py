from flask import Flask, render_template, request, url_for, redirect, jsonify
import sys
sys.path.append('../')

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

@app.route('/mainshow')
def mainshow():
    return render_template('mainshow_director.html')

@app.route('/show', methods=['GET'])
def show():
    type_ = request.args.get('type_', None)
    if type_ == 'years':
        return render_template('show_year.html')
    elif type_ == 'director':
        return render_template('show_director.html')
    else:
        return render_template('show_production.html')

if __name__ == '__main__':
    app.run(debug=True)
