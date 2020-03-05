from flask import Flask, request, make_response
from flask.views import MethodView
from pymongo import MongoClient


client = MongoClient(host='mongo', port=27017, username='docker', password='docker')
db = client['test']


class TestResource(MethodView):

    def post(self):
        db['test'].insert_one(request.json)
        return make_response({}, 200)


app = Flask(__name__)

app.add_url_rule('/test', view_func=TestResource.as_view('test'))
print('flask mongo is ready')
