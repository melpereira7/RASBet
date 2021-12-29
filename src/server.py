from flask import Flask
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)


class Info(Resource):
    @staticmethod
    def get():
        f = open('./bettingAPI.json')
        data = json.load(f)
        return data, 200


api.add_resource(Info, '/info')

if __name__ == '__main__':
    app.run()
