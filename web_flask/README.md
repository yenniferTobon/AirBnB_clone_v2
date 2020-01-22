HBNB

## 0x04. AirBnB clone - Web framework
### Description

### Files

| File | Description |
| ------ | ------ |
| Write a blog post explaining what happens when you type https://www.holbertonschool.com in your browser and press Enter.

#Resources
## Read or watch:
* What is a Web Framework?
* A Minimal Application
* Routing (except “HTTP Methods”)
* Rendering Templates
* Synopsis
* Variables
* Comments
* Whitespace Control
* List of Control Structures (read up to “Call”)
* Flask
* Jinja

##General
* What is a Web Framework
* How to build a web framework with Flask
* How to define routes in Flask
* What is a route
* How to handle variables in a route
* What is a template
* How to create a HTML response in Flask by using a template
* How to create a dynamic template (loops, conditions…)
* How to display in HTML data from a MySQL database

* [web_flask](web_flask) - contains Flask, templates, and static files
  * [`__init__.py`](web_flask/__init__.py) - import Flask and create a Flask instance
  * [0-hello_route.py](web_flask/0-hello_route.py) - script that starts a Flask web application where route `/` displays 'Hello HBNB!'
  * [1-hbnb_route.py](web_flask/1-hbnb_route.py) - script that starts a Flask web application where route `/` displays 'Hello HBNB~' and route `/hbnb` displays 'HBNB'
  * [2-c_route.py](web_flask/2-c_route.py) - script that starts a Flask web application where route `/` displays 'Hello HBNB!', `/hbnb` displays 'HBNB', `/c/<text>` displays 'C' followed by the value of the text variable (replace underscore `_` symbols with a space ` `
  * [3-python_route.py](web_flask/3-python_route.py) - script that starts a Flask web application where route `/` displays 'Hello HBNB!', `/hbnb` displays 'HBNB', `/c/<text>` displays 'C' followed by the value of the text variable (replace underscore `_` symbols with a space ` `, `/python/(<text>)` displays 'Python ', followed by the value of the text variable (replace underscore `_` symbols with a space ` `) where the default value of `text` is 'is cool'
  * [4-number_route.py](web_flask/4-number_route.py) - script that starts a Flask web application where route `/` displays 'Hello HBNB!', `/hbnb` displays 'HBNB', `/c/<text>` displays 'C' followed by the value of the text variable (replace underscore `_` symbols with a space ` `, `/python/(<text>)` displays 'Python ', followed by the value of the text variable (replace underscore `_` symbols with a space ` `) where the default value of `text` is 'is cool', `/number/<n>` displays '`n` is a number' only if n is an integer
  * [5-number_template.py](web_flask/5-number_template.py) - script that starts a Flask web application where route `/` displays 'Hello HBNB!', `/hbnb` displays 'HBNB', `/c/<text>` displays 'C' followed by the value of the text variable (replace underscore `_` symbols with a space ` `, `/python/(<text>)` displays 'Python ', followed by the value of the text variable (replace underscore `_` symbols with a space ` `) where the default value of `text` is 'is cool', `/number/<n>` displays '`n` is a number' only if n is an integer, `/number_template/<n>` displays an HTML page only if `n` is an integer
  * [6-number_odd_or_even.py](web_flask/6-number_odd_or_even.py) - script that starts a Flask web application where route `/` displays 'Hello HBNB!', `/hbnb` displays 'HBNB', `/c/<text>` displays 'C' followed by the value of the text variable (replace underscore `_` symbols with a space ` `, `/python/(<text>)` displays 'Python ', followed by the value of the text variable (replace underscore `_` symbols with a space ` `) where the default value of `text` is 'is cool', `/number/<n>` displays '`n` is a number' only if n is an integer, `/number_template/<n>` displays an HTML page only if `n` is an integer, `/number_odd_or_even/<n>` displays an HTML page only if `n` is an integer where `H1` tag includes 'Number: `n` is `even|odd`' in `BODY` tag
  * [7-states_list.py](web_flask/7-states_list.py) - script that starts a Flask web application where route `/states_list` displays an HTML page with `H1` tag: “States”, `UL` tag: list of all State objects present in DBStorage sorted by name (A->Z), `LI` tag: description of one `State: <state.id>: <B><state.name></B>`
  * [8-cities_by_states.py](web_flask/8-cities_by_states.py) - script that starts a Flask web application where route `/cities_by_states` displays an HTML page with `H1` tag: “States”, `UL` tag: list of all State objects present in DBStorage sorted by name (A->Z), `LI` tag: description of one `State: <state.id>: <B><state.name></B>`, `LI` tag: description of one `City: <city.id>: <B><city.name></B>`
  * [9-states.py](web_flask/9-states.py) - script that starts a Flask web application where route `/states` displays an HTML page with `H1` tag: “States”, `UL` tag: list of all State objects present in DBStorage sorted by name (A->Z), `LI` tag: description of one `State: <state.id>: <B><state.name></B>`; route `/states/<id>`displays an HTML page where if a State object is found with this id: `H1` tag: “State: ”, `H3` tag: “Cities:”, `UL` tag: with the list of City objects linked to the State sorted by name (A->Z), `LI` tag: description of one `City: <city.id>: <B><city.name></B>`; Otherwise: `H1` tag: “Not found!”
  * [10-hbnb_filters.py](web_flask/10-hbnb_filters.py) - script that starts a Flask web application and defines route `/hbnb_filters` to display an HTML page like below:

## Authors

Yennifer Marcela Tobon.
