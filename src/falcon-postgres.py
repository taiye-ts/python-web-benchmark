from falcon import API
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


class TestResource:

    def on_post(self, request, response):

        cursor = connection.cursor()
        cursor.execute("INSERT INTO test (data) VALUES (%s)", (json.dumps(
            to_dict(request.stream.read(request.content_length or 0))
        ), ))
        connection.commit()
        cursor.close()


app = API()
app.add_route('/test', TestResource())
print('started falcon-postgres server')
