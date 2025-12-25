import mysql.connector as mysql
import creds
import os
import dotenv

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)
cursor.execute('SELECT * FROM students')
data = cursor.fetchall()
print(data)