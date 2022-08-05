from mysql_connector import connect_db
import mysql.connector
import os

USERNAME = os.environ['MYSQL_USERNAME']
PASSWORD = os.environ['MYSQL_PASSWORD']

conn = mysql.connector.connect(
host="localhost",
user=USERNAME,
password=PASSWORD
)

c = conn.cursor()
c.execute("SHOW DATABASES;")

print(c)