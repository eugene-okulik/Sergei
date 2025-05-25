# Есть такой список:
#
# temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
#                 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
#
# С помощью функции map или filter создайте из этого списка новый список с
# жаркими днями. Будем считать жарким всё, что выше 28.
# Распечатайте из нового списка самую высокую температуру, самую низкую и
# среднюю.

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

# hot_days = []
# for x in temperatures:
#     if x > 28:
#         hot_days .append(x)
#
# Или
hot_days = list(filter(lambda x: x > 28, temperatures))

print("Жаркие дни:", hot_days)
print("Максимальная температура:", max(hot_days))
print("Минимальная температура:", min(hot_days))
print("Средняя температура:", round(sum(hot_days) / len(hot_days), 2))

# Или
hot_days = map(lambda x: x if x > 28 else None, temperatures)
hot_days = list(filter(None, hot_days))

print("Жаркие дни:", hot_days)
print("Максимальная:", max(hot_days))
print("Минимальная:", min(hot_days))
print("Средняя:", round(sum(hot_days) / len(hot_days), 1))
