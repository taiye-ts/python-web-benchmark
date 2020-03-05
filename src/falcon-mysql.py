from falcon import API
import pymysql
import json

connection = pymysql.connect(
    host='mysql',
    user='docker',
    password='docker',
    db='docker',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


class TestResource:

    def on_post(self, request, response):
        with connection.cursor() as cursor:
            sql = "INSERT INTO test (data) VALUES (%s)"
            cursor.execute(sql, (json.dumps(request.media, )))
        connection.commit()

app = API()
app.add_route('/test', TestResource())
print('started falcon-mysql server')
