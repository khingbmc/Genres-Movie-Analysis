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

@app.route('/marvel')
def marvel():
    return render_template('marvel.html')
@app.route('/dc')
def dc():
    return render_template('dc.html')
@app.route('/columbia')
def columbia():
    return render_template('columbia.html')
@app.route('/disney')
def disney():
    return render_template('disney.html')

@app.route('/nolan')
def nolan():
    return render_template('christopher.html')
@app.route('/bay')
def bay():
    return render_template('michael.html')
@app.route('/steven')
def steven():
    return render_template('steven.html')
@app.route('/toro')
def toro():
    return render_template('guillermo.html')
if __name__ == '__main__':
    app.run(debug=True)
