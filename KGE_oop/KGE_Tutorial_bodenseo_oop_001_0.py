#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
KGE Bremen
2024-07-14

Tutorial https://www.python-kurs.eu/python_OOP.php
"""

x = [3, 6, 9]
y = [45, "abc"]

print('x = ', x, ' x ist von der Klasse : ', type(x))

print('x[1] = ', x[1])

x[1] = 99

print('x = ', x)
print('x[1] = ', x[1])

x.append(42)

print('x = ', x)

print('y = ', y,  ' y ist von der Klasse : ', type(y))
last = y.pop()

print('last y = ', last)

print('y nach pop = ', y)


