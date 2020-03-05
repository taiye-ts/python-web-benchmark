import pymysql.cursors

connection = pymysql.connect(
    host='mysql',
    user='docker',
    password='docker',
    db='docker',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    sql = "CREATE TABLE test (id SERIAL PRIMARY KEY not NULL, data JSON not NULL)"
    cursor.execute(sql)

connection.commit()
