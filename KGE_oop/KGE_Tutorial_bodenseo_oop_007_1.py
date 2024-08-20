#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
KGE Bremen
2024-07-15

Tutorial https://www.python-kurs.eu/python_OOP.php
"""

class Roboter:
    def __init__(self, name, baujahr):
        self.name = name
        self.baujahr = baujahr
    def SageHallo(self):
        if hasattr(self, 'name'):
            print("Hallo, mein Name ist ", self.name)
        else:
            print("Ich habe keinen Namen !")
    def NeuerName(self, name):
        self.name = name
    def NeuesBaujahr(self, baujahr):
        self.baujahr = baujahr
        

x = Roboter("Marvin", 1979)
x.name = "Marvin2"

y = Roboter('unbekannt', 2000)
y.NeuerName("Caliban")

x.SageHallo()
y.SageHallo()
