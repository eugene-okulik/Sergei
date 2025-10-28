import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
# 1. Добавляем студента
cursor.execute(
    "INSERT INTO students (name, second_name) VALUES (%s, %s)",
    ("Сергей", "Добреньков3")
)
student_id = cursor.lastrowid
print(f"Added student id={student_id}")

cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
print("Student record:", cursor.fetchone())

# 2. Добавляем группу
cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
    ("Sergei_group", "jun 2025", "dec 2026")
)
group_id = cursor.lastrowid
print(f"Added group id={group_id}")

cursor.execute("SELECT * FROM `groups` WHERE id=%s", (group_id,))
print("Group record:", cursor.fetchone())

# 3. Привязываем студента к группе
cursor.execute("""
UPDATE students SET group_id=%s WHERE id=%s""", (group_id, student_id))
db.commit()
print("Linked student to group")

# 4. Добавляем книги
books = [
    ("Server 2019", student_id),
    ("SQL Server 2025", student_id),
    ("Python 2025", student_id)
]
cursor.executemany("""
INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)""", books)
db.commit()
print("Added books for student")

cursor.execute("""
SELECT * FROM books WHERE taken_by_student_id=%s""", (student_id,))
print("Books:", cursor.fetchall())

# 5. Добавляем предметы
subjects = [("SQL subject",), ("Microsoft subject",), ("Python subject",)]
cursor.executemany("INSERT INTO subjects (title) VALUES (%s)", subjects)
db.commit()

# Получаем их id по title
cursor.execute("""
SELECT id, title FROM subjects
WHERE title IN ('SQL subject', 'Microsoft subject', 'Python subject')
""")
subjects_data = cursor.fetchall()
print("Subjects:", subjects_data)

# Преобразуем список словарей в словарь "название → id"
subject_ids = {subj["title"]: subj["id"] for subj in subjects_data}

# Сохраняем id предметов в переменные
sql_subject_id = subject_ids["SQL subject"]
ms_subject_id = subject_ids["Microsoft subject"]
py_subject_id = subject_ids["Python subject"]
print("Subject IDs:", subject_ids)

# 6. Добавляем уроки
lessons = [
    ("lesson 1", sql_subject_id),
    ("lesson 2", sql_subject_id),
    ("lesson 3", ms_subject_id),
    ("lesson 4", ms_subject_id),
    ("lesson 5", py_subject_id),
    ("lesson 6", py_subject_id)
]
cursor.executemany("""
INSERT INTO lessons (title, subject_id) VALUES (%s, %s)""", lessons)
db.commit()
print("Added lessons")

cursor.execute("""
SELECT id, subject_id FROM lessons 
WHERE subject_id IN (%s, %s, %s )
ORDER BY subject_id, id
""", (sql_subject_id, ms_subject_id, py_subject_id))
lessons_data = cursor.fetchall()
print("Lessons:", lessons_data)

# Группируем уроки по subject_id
lessons_by_subject = {}
for row in lessons_data:
    subj_id = row["subject_id"]
    lessons_by_subject.setdefault(subj_id, []).append(row["id"])

print("Lessons grouped by subject:", lessons_by_subject)
# 7. Добавляем оценки
marks = [
    (4, lessons_by_subject[sql_subject_id][0], student_id),
    (5, lessons_by_subject[sql_subject_id][1], student_id),
    (3, lessons_by_subject[ms_subject_id][0], student_id),
    (4, lessons_by_subject[ms_subject_id][1], student_id),
    (5, lessons_by_subject[py_subject_id][0], student_id),
    (5, lessons_by_subject[py_subject_id][1], student_id)
]
cursor.executemany("""
INSERT INTO marks (value, lesson_id, student_id) 
VALUES (%s, %s, %s )""", marks)
db.commit()
print("Added marks")

cursor.execute("SELECT * FROM marks WHERE student_id=%s", (student_id,))
print("Marks for student:", cursor.fetchall())

# Завершение
db.close()
print("🎉 All operations completed successfully!")
