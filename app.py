import flask
import os
import logging
# logging.basicConfig(level=10,
#                     format='%(asctime)s %(levelname)s:%(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filename='app.log',
#                     filemode='w')

from flask import Flask, request, jsonify, render_template
# making an instance of the Flask class
app = Flask(__name__)
@app.route('/')
def welcome():
    return "<html><h1>This is HTML file</h1></html>"

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/aboutus')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"hii {name}"
    return render_template('form.html')
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"hii {name}"
    return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "pass"
    else:
        res = "fail"
    return render_template('success.html', result=res)


if __name__ == '__main__':
    app.run(debug=True)

