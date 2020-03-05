import psycopg2


connection = psycopg2.connect(
    host='postgres',
    port=5432,
    user='docker',
    password='docker',
    database='docker'
)

cursor = connection.cursor()
cursor.execute("CREATE TABLE test (id SERIAL PRIMARY KEY not NULL, data JSONB not NULL)")
connection.commit()
cursor.close()
