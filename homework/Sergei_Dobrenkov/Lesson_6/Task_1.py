#  Задание №1
#  Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в
#  тексте “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
#  Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
#  и после этого выводит получившийся текст на экран. Знаки препинания не
#  должны оказаться внутри слова. Если после слова идет запятая или точка,
#  этот знак препинания должен идти после того же слова,
#  но уже преобразованного.

import string
#  print(string.punctuation)

text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
words = text.split()  # Разбиваем текст на слова по пробелам.
new_words = []

for word in words:
    if word[-1] in string.punctuation:  # Проверяем, заканчивается ли слово на
        # знак препинания
        new_word = word[:-1] + 'ing' + word[-1]  # Берём всё слово, кроме
        # последнего символа, Прибавляем 'ing',
        # И снова добавляем в конец исходный знак препинания
    else:
        new_word = word + 'ing'
    new_words.append(new_word)  # Добавляем новое слово в список
new_text = ' '.join(new_words)  # Объединяем в одну строку, разделяя пробелами
print(new_text)
