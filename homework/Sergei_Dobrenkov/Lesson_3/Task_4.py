#Даны катеты прямоугольного треугольника.
#Найти его гипотенузу и площадь

import math

leg_a = 3
leg_b = 4
hypotenuse = math.sqrt((leg_a * leg_a) + (leg_b * leg_b))
print(hypotenuse )
square = (leg_a * leg_b / 2)
print(square)
