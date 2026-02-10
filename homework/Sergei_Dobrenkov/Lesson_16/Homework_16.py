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

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))

CSV_PATH = os.path.join(PROJECT_ROOT, "eugene_okulik",
                        "Lesson_16", "hw_data", "data.csv")


with open(CSV_PATH, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute(
            """
            SELECT 1
            FROM students
            join `groups`on students.group_id = `groups`.id
            join books on students.id = books.taken_by_student_id
            join marks on students.id= marks.student_id
            join lessons on lessons.id = marks.lesson_id
            join subjects on subjects.id = lessons.subject_id
            WHERE
                students.name = %s
                AND students.second_name = %s
                AND `groups`.title = %s
                AND books.title = %s
                AND subjects.title = %s
                AND lessons.title = %s
                AND marks.value = %s
            LIMIT 1
            """,
            (
                row["name"],
                row["second_name"],
                row["group_title"],
                row["book_title"],
                row["subject_title"],
                row["lesson_title"],
                row["mark_value"]
            )
        )

        result = cursor.fetchone()

        if result is None:
            print(
                "В базе нет данных: "
                f"name={row['name']}, second_name={row['second_name']}, "
                f"group={row['group_title']}, mark={row['mark_value']}"
            )
db.close()
