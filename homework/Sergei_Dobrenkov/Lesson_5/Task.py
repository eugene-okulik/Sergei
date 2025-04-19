#  Задание 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person #  создание из списка переменных
print(name)
print(last_name)
print(city)
print(phone)
print(country)

#  Задание 2
text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'
#  С помощью срезов и метода index получите из каждой строки с результатом число,
#  прибавьте к полученному числу 10, результат сложения распечатайте.
#  index1 = text1.index(":")+1
#  index2 = text2.index(":")+1
#  index3 = text3.index(":")+1
num1 = int(text1[text1.index(":")+1:])+10
num2 = int(text2[text2.index(":")+1:])+10
num3 = int(text3[text3.index(":")+1:])+10
print(num1)
print(num2)
print(num3)

#  Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ','.join(students)
subjects = ','.join(subjects)
print('Students ' + students + ' study these subjects: ' + subjects )
