#!/usr/bin/python3
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """url- 0.0.0.0/5000: display “Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """url-0.0.0.0/5000/hbnb: display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """url- 0.0.0.0/5000/c/<text>: display “C ” y value of the text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text=None):
    """"url- 0.0.0.0/5000/python/(<text>): display “Python" y text"""
    if text is None:
        text = 'is cool'
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """url-0.0.0.0/5000/number/<n>: display “n is a number” if is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """url-0.0.0.0/5000/number_template/<n>: display HTML page if an integer"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
