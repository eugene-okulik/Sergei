# Напишите программу. Есть две переменные, salary и bonus. Salary - int,
# bonus - bool. Спросите у пользователя salary.
# А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
#
# Примеры результатов:
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

import random

salary_input = input("Your salary: ")
salary = int(salary_input)

bonus = random.choice([True, False])

if bonus:
    bonus_amount = random.randint(100, 1000)
    pay = salary + bonus_amount
else:
    pay = salary
print(f"{salary}, {bonus} - '${pay}'")
