import csv
import os
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor()

CSV_PATH = r"D:\Projects\Sergei\homework\eugene_okulik\Lesson_16\data.csv"

with open(CSV_PATH, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"]
        second_name = row["last"]

        cursor.execute(
            """
            SELECT 1
            FROM students
            WHERE name = %s AND second_name = %s
            LIMIT 1
            """,
            (name, second_name)
        )

        if cursor.fetchone() is None:
            print(
                f"В базе нет данных: "
                f"name='{name}', second_name='{second_name}'"
            )
db.close()
