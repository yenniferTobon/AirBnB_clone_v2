#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage
from models import state
app = Flask(__name__)


@app.teardown_appcontext
def close(error):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """url: 0.0.0.0:5000/states_list: display a HTML page: """
    list_states = storage.all("State")
    storage.close()
    return render_template('7-states_list.html', list_states=list_states)


"""web application must be listening on 0.0.0.0, port 5000"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
