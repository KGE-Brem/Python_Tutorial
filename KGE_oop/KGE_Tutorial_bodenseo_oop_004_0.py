#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
KGE Bremen
2024-07-15

Tutorial https://www.python-kurs.eu/python_OOP.php
"""

class Roboter:
    pass


def f(x):
    if hasattr(f, "zaehler"):
        f.zaehler = f.zaehler + 1
    else:
        f.zaehler = 0
    return x+3

for i in range(3):
    f(i)

if hasattr(f, "zaehler"):
    print('fuer i = ', i, 'ist f.zaehler = ',f.zaehler)

