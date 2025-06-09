# Напишите программу: Есть функция которая делает одну из арифметических
# операций с переданными ей числами (числа и операция передаются в аргументы
# функции).
# Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая
# операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

def operation_manager(func):
    def wrapper(first, second, operation=None):
        # Проверяем условия по числам, определяем операцию
        if first == second:
            op = '+'
        elif first > second:
            op = '-'
        elif second > first:
            op = '/'
        if first < 0 or second < 0:
            op = '*'
        return func(first, second, op)
    return wrapper


@operation_manager
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        if second == 0:
            return "Ошибка: деление на ноль"
        return first / second
    else:
        return "Неизвестная операция"


# Ввод чисел от пользователя
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

result = calc(a, b)
print("Результат:", result)
