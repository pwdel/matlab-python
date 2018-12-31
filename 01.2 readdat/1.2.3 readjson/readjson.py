# readjson.py
# json documentation https://docs.python.org/3/library/json.html
import json

import json as json

path = 'sample.json' # path to our document containing json
thing = open(path) # put the json document into thing
data = json.load(thing) # use json.load to parse json into a list

data.keys() # get the first key

data # displays entire json Object

data['glossary']['title'] # displays the first sub-item, 'title' value

data['glossary']['GlossDiv'] # displays the contents of sub-item 'GlossDiv'

data['glossary']['GlossDiv']['GlossList'] # displays 'GlossList' within 'GlossDiv'

"""
Ultimately in most analytics operations, the objective is going to be to take
a set of data stored in json and turn it in another format.

The most simple format would be simply a python object.  This would be equivalent
to the "variables" that we show in the Matlab toolbox view.  However in python
the variables are invisible to the user, unless you ask to display them.

The advantage of viewing variables is two fold:
1. You can see what the variables contain quickly without needing to call them.
2. You can see how much memory variables are taking up.

We can go through some strategies to increase performance in terms of memory usage
in future parts of this repo as well as strategies for viewing variables.

"""
