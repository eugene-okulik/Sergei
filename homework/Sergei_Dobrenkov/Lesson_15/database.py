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
    ("Сергей", "Добреньков5"))
db.commit()
student_id = cursor.lastrowid
print(f"Added student id={student_id}")

cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
print("Student record:", cursor.fetchone())

# 2. Добавляем группу
cursor.execute("""
INSERT INTO `groups` (title, start_date, end_date)
VALUES (%s, %s, %s)""",
               ("Sergei_group", "jun 2025", "dec 2026"))
db.commit()
group_id = cursor.lastrowid
print(f"Added group id={group_id}")

cursor.execute("SELECT * FROM `groups` WHERE id=%s", (group_id,))
print("Group record:", cursor.fetchone())

# 3. Привязываем студента к группе
cursor.execute("""
UPDATE students SET group_id=%s WHERE id=%s""", (group_id, student_id))
db.commit()
print(f"Linked student {student_id} to group {group_id}")

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
subject_titles = ["SQL subject", "Microsoft subject", "Python subject"]
subject_ids = {}
for title in subject_titles:
    cursor.execute("""
    INSERT INTO subjects (title) VALUES (%s)""", (title,))
    db.commit()
    subject_id = cursor.lastrowid
    subject_ids[title] = subject_id
    print(f"Added subjects for student: {title}, id={subject_id}")

print("Subjects with ID:", subject_ids)

# 6. Добавляем уроки
lessons_to_add = [
    ("lesson 1", subject_ids["SQL subject"]),
    ("lesson 2", subject_ids["SQL subject"]),
    ("lesson 3", subject_ids["Microsoft subject"]),
    ("lesson 4", subject_ids["Microsoft subject"]),
    ("lesson 5", subject_ids["Python subject"]),
    ("lesson 6", subject_ids["Python subject"]),
]

lesson_ids = []

for title, subj_id in lessons_to_add:
    cursor.execute("""
    INSERT INTO lessons (title, subject_id)
    VALUES (%s, %s)
    """, (title, subj_id))
    db.commit()
    lesson_id = cursor.lastrowid
    lesson_ids.append(lesson_id)
    print(f"Added lessons: {title}, id={lesson_id}, subject_id={subj_id}")

print("Added lessons with (id):", lesson_ids)

# 7. Добавляем оценки
marks = [
    (4, lesson_ids[0], student_id),
    (5, lesson_ids[1], student_id),
    (3, lesson_ids[2], student_id),
    (4, lesson_ids[3], student_id),
    (5, lesson_ids[4], student_id),
    (5, lesson_ids[5], student_id),
]
cursor.executemany("""
INSERT INTO marks (value, lesson_id, student_id)
VALUES (%s, %s, %s )""", marks)
db.commit()
print("Added marks")

cursor.execute("""
SELECT * FROM marks WHERE student_id=%s""", (student_id,))
print("Marks for student:", cursor.fetchall())

# 8. Вся информация о студенте
cursor.execute("""
SELECT students.name, students.second_name,
       groups.title AS group_name, groups.start_date, groups.end_date,
       books.title AS book_title,
       lessons.title AS lesson_title,
       subjects.title AS subject_title,
       marks.value AS mark
FROM students
JOIN `groups` ON students.group_id = groups.id
JOIN books ON students.id = books.taken_by_student_id
JOIN marks ON students.id = marks.student_id
JOIN lessons ON lessons.id = marks.lesson_id
JOIN subjects ON subjects.id = lessons.subject_id
WHERE students.id = %s
""", (student_id,))
result = cursor.fetchall()

print("\n Вся информация о студенте")
for row in result:
    print(row)

# Завершение
cursor.close()
db.close()
print("🎉 All operations completed successfully!")
