import os
from datetime import datetime, timedelta

# строим путь динамически, чтобы код работал в любом окружении
base_dir = os.path.dirname(__file__)   # папка, где лежит текущий скрипт
file_path = os.path.join(base_dir, "homework",
                         "eugene_okulik", "hw_13", "data.txt")

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    number, rest = line.split(". ", 1)
    date_str, instruction = rest.split(" - ", 1)
    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

    if "неделю позже" in instruction:
        print(f"{number}: {date + timedelta(weeks=1)}")
    elif "день недели" in instruction:
        print(f"{number}: {date.strftime('%A')}")
    elif "дней назад" in instruction:
        print(f"{number}: {(datetime.now() - date).days} дней назад")
