from flask import Flask
import logging
import json
import pymysql

app = Flask(__name__)

dbhost = '10.0.30.52'
dbuser = 'root'
dbpassword = 'Welcome123!@'
dbname = 'mysql'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

conn = pymysql.connect(host=dbhost, user=dbuser, password=dbpassword, db=dbname, connect_timeout=5)

@app.route("/")
def list_data():
    try:
        cursor = conn.cursor()
        sql = "select version(), current_date, user()"
        cursor.execute(sql)
    except Exception as ex:
        logger.error("ERROR: Could not fetch data.")
        logger.error(e)

    logger.info("SUCCESS: Fetching data succeeded")

    results = cursor.fetchall()
    json_data = json.dumps(results, default=str)

    cursor.close()

    return json_data

print(list_data())

if __name__ == "__main__":
    app.run(host='0.0.0.0')
