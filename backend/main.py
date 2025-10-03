from flask import Flask
import os, psycopg2

app = Flask(__name__)

@app.route("/db", methods=['GET'])
def get_db():
	return ' '.join(map(str, get_records()))

def get_db_cursor():
  pg_connection_dict = {
    'dbname': os.getenv('POSTGRES_DB', "Please set POSTGRES_DB"),
    'user':os.getenv('POSTGRES_USER', "Please set POSTGRES_USER"),
    'password': os.getenv('POSTGRES_PASSWORD', "Please set POSTGRES_PASSWORD"),
    'host': os.getenv('POSTGRES_HOST', "Please set POSTGRES_HOST")
	}
  connection = psycopg2.connect(**pg_connection_dict)
  return connection.cursor()

def get_records():
  cursor=get_db_cursor()
  query=f"SELECT * FROM {os.getenv('POSTGRES_TABLE', 'Please set POSTGRES_TABLE')};"
  cursor.execute(query)
  return cursor.fetchall()


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=os.getenv('PORT_BACKEND', 80))
