# Обработка даты
# Дана такая дата: "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:
# 1. Распечатайте полное название месяца из этой даты
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"

import datetime

my_date = 'Jan 15, 2023 - 12:05:33'

python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')
name_month = python_date.strftime("%B")
date_in_format = python_date.strftime('%d.%m.%Y, %H:%M')

# print(python_date)
print("Полное название месяца:", name_month)
print("Форматированная дата:", date_in_format)
