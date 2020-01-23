#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage
from models import state
app = Flask(__name__)


@app.teardown_appcontext
def close(error):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """url: 0.0.0.0:5000/states_list: display a HTML page: """
    list_states = storage.all("State")
    list_cities = storage.all("City")
    return render_template('8-cities_by_states.html',
                           list_states=list_states, list_cities=list_cities)


"""web application must be listening on 0.0.0.0, port 5000"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
