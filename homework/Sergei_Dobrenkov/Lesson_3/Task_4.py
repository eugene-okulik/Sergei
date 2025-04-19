# Даны катеты прямоугольного треугольника.
# Найти его гипотенузу и площадь

import math

leg_a = 5
leg_b = 5
hypotenuse = math.sqrt((leg_a * leg_a) + (leg_b * leg_b))
print(hypotenuse)
square = (leg_a * leg_b / 2)
print(square)


leg_a = 3
leg_b = 4
kat1 = leg_a * leg_a
kat2 = leg_b * leg_b
hypotenuse = math.sqrt(kat1 + kat2)
print(hypotenuse)