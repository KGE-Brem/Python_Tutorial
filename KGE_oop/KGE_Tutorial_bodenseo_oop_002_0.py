#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
KGE Bremen
2024-07-14

Tutorial https://www.python-kurs.eu/python_OOP.php
"""

class Roboter:
    pass

x = Roboter()
y = Roboter()

y2 = y

print('y == y2 ? ', y == y2)
print('y == x  ? ', y == x)

x.name = 'Marvin'
x.baujahr = 1979

y.name = 'Caliban'
y.baujahr = 1993

print('x.name = ',x.name,'x.baujahr = ', x.baujahr, type(x))
print('y.name = ',y.name,'y.baujahr = ', y.baujahr, type(y))

