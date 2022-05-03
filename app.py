from cgi import test
from flask import Flask, request
from flask import render_template

from scraping_test import getQuotes

app = Flask(__name__)


@app.route('/')

def index():

  return render_template('index.html')

@app.route('/getQuote/')

def my_link():

  quote = getQuotes()['quote']

  return quote

if __name__ == "__main__":
    app.run(debug=True, port=5000)