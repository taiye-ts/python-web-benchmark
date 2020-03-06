from falcon import API
from pymongo import MongoClient

from message import to_dict

client = MongoClient(host='mongo', port=27017, username='docker', password='docker')
db = client['test']


class TestResource:

    def on_post(self, request, response):
        db['test'].insert_one(
            to_dict(request.stream.read(request.content_length or 0))
        )


app = API()
app.add_route('/test', TestResource())
print('started falcon-mongo server')
