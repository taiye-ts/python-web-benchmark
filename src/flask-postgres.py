from flask import Flask, request, make_response
from flask.views import MethodView
import psycopg2
import json
from message import to_dict


connection = psycopg2.connect(
    host='postgres',
    port=5432,
    user='docker',
    password='docker',
    database='docker'
)


class TestResource(MethodView):

    def post(self):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO test (data) VALUES (%s)", (json.dumps(
            to_dict(request.data)
        ), ))
        connection.commit()
        return make_response({}, 200)


app = Flask(__name__)

app.add_url_rule('/test', view_func=TestResource.as_view('test'))
print('flask postgres is ready')
