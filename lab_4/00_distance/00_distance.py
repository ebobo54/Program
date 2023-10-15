#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = dict()

M = sites['Moscow']
L = sites['London']
P = sites['Paris']

Moscow_Paris = ((M[0] - L[0]) ** 2 + (M[1] - L[1]) ** 2) **  0.5
Moscow_London = ((M[0] - L[0]) ** 2 + (M[1] - L[1]) ** 2) **  0.5
Paris_London = ((P[0] - L[0]) ** 2 + (P[1] - L[1]) ** 2) **  0.5

distances['Moscow'] = {}
distances['Moscow']['London']=Moscow_London
distances['Moscow']['Paris']=Moscow_Paris

distances['London'] = {}
distances['London']['Paris'] = Paris_London
distances['London']['Moscow'] = Moscow_London

distances['Paris'] = {}
distances['Paris']['London'] = Paris_London
distances['Paris']['Moscow'] = Moscow_Paris
# TODO здесь заполнение словаря

result = {'Moscow-London' : distances['Moscow']['London'], 'Moscow-Paris' : distances['Moscow']['Paris'], 'Paris-London' : distances['Paris']['London']}

print(result)




