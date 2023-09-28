from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import json

app = Flask(__name__)
cores = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

file = open("data.json")
mockData = json.load(file)

class getData(Resource):
    def get(self):
        return jsonify(mockData)

api.add_resource(getData, "/getData")

if (__name__ == "__main__"):
    print('run mockBackend Server')
    app.run(host='0.0.0.0')

file.close()
