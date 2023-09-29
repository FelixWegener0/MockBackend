from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import json
from time import sleep

app = Flask(__name__)
cores = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

mockDatabase = open("mockdatabase.json")
mockDatabasejson = json.load(mockDatabase)

class getThisDaysTempValues(Resource):
    def get(self):
        return jsonify(mockDatabasejson["data"])

class getCurrentTemp(Resource):
    def get(self):
        sleep(5)
        return jsonify(25)
    
class getCurrentHumid(Resource):
    def get(self):
        sleep(5)
        return jsonify(45)

api.add_resource(getThisDaysTempValues, "/getThisDaysTempValues")
api.add_resource(getCurrentTemp, "/getCurrentTemp")
api.add_resource(getCurrentHumid, "/getCurrentHumid")

if (__name__ == "__main__"):
    print('run mockBackend Server')
    app.run(host='0.0.0.0')

mockDatabase.close()
