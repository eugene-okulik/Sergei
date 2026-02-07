import os
import re

# --- ввод от пользователя ---
path = input("Введите путь к файлу или папке с логами:\n").strip()
search_text = input("Введите текст для поиска:\n").strip()

# --- регулярка для времени ---
TIME_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}")

def get_files(path):
    if os.path.isfile(path):
        return [path]
    elif os.path.isdir(path):
        return [
            os.path.join(path, f)
            for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f))
        ]
    else:
        raise FileNotFoundError("Указанный путь не существует")

def extract_time(line):
    match = TIME_PATTERN.search(line)
    return match.group() if match else "Время не найдено"

def extract_context(line, word, before=5, after=5):
    words = line.split()
    for i, w in enumerate(words):
        if word in w:
            start = max(0, i - before)
            end = min(len(words), i + after + 1)
            return " ".join(words[start:end])
    return line.strip()

def analyze_file(file_path):
    results = []
    with open(file_path, encoding="utf-8", errors="ignore") as file:
        for line_number, line in enumerate(file, start=1):
            if search_text in line:
                results.append({
                    "file": os.path.basename(file_path),
                    "line": line_number,
                    "time": extract_time(line),
                    "context": extract_context(line, search_text)
                })
    return results

# --- запуск ---
try:
    files = get_files(path)
except FileNotFoundError as e:
    print(e)
    exit(1)

found = False

for file_path in files:
    matches = analyze_file(file_path)
    for match in matches:
        found = True
        print("=" * 80)
        print(f"Файл: {match['file']}")
        print(f"Строка: {match['line']}")
        print(f"Время: {match['time']}")
        print("Фрагмент ошибки:")
        print(match['context'])

if not found:
    print("Совпадений не найдено.")
