import flask
from flask import request, jsonify
from pymongo import MongoClient

try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB")

db = conn.milijuliyatayat
collection = db.location

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'lattitude': '8737263',
     'longitude': '23322'},

    {'id': 1,
     'lattitude': '6252687982',
     'longitude': '6252687982'
     },

    {'id': 2,
     'lattitude': '6252687982',
     'longitude': '6252687982'
    }
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Sonika</h1>
<p>Milijuli Yatayat</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/datastore', methods=['GET'])
def api_all():
    return jsonify(books)
app.run()