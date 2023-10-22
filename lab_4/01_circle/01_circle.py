#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
# TODO здесь ваш код
pi = 3.1415926
radius = 42
s = pi * radius ** 2
print('s=  ', s)
# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
# TODO здесь ваш код
distance_1 = (point_1[0] ** 2 + point_1[1] ** 2)
is_inside_1 = distance_1 <= radius
print(f'Точка 1 внутри круга: {is_inside_1}')
# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# TODO здесь ваш код
distance_2 = (point_2[0] ** 2 + point_2[1] ** 2)
is_inside_2 = distance_2 <= radius
print(f'Точка 2 внутри круга: {is_inside_2}')
# Пример вывода на консоль:
#
# 77777.7777
# False
# False


