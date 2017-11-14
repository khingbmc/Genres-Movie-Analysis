from flask import Flask, render_template, request, url_for, redirect, jsonify
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
    return type_

if __name__ == '__main__':
    app.run(debug=True)
