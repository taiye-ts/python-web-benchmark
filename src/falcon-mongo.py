from falcon import API
from pymongo import MongoClient


client = MongoClient(host='mongo', port=27017, username='docker', password='docker')
db = client['test']


class TestResource:

    def on_post(self, request, response):
        db['test'].insert_one(request.media)


app = API()
app.add_route('/test', TestResource())
print('started falcon-mongo server')
