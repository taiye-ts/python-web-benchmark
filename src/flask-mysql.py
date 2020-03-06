from flask import Flask, request, make_response
from flask.views import MethodView
import pymysql
import json

from message import to_dict

connection = pymysql.connect(
    host='mysql',
    user='docker',
    password='docker',
    db='docker',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

class TestResource(MethodView):

    def post(self):
        with connection.cursor() as cursor:
            sql = "INSERT INTO test (data) VALUES (%s)"
            cursor.execute(sql, (json.dumps(to_dict(request.data))))
        connection.commit()
        return make_response({}, 200)


app = Flask(__name__)

app.add_url_rule('/test', view_func=TestResource.as_view('test'))
print('flask mysql is ready')
