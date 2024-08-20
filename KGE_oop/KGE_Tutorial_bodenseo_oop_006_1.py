#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
KGE Bremen
2024-07-15

Tutorial https://www.python-kurs.eu/python_OOP.php
"""

class Roboter:
    def SageHallo(self):
        if hasattr(self,'name'):
            print("Hallo, mein Name ist " + self.name)
        else:
            print("Hallo, ich habe keinen Namen")
    def SetzeNamen(self, name):
        self.name = name
    def SetzeBaujahr(self, baujahr):
        self.baujahr = baujahr
    

x = Roboter()
x.SetzeNamen('Marvin')
x.SetzeBaujahr(1979)

x.SageHallo()

y = Roboter()
#y.name = 'Caliban'
#y.SetzeNamen('Caliban')
y.SetzeBaujahr(1993)

y.SageHallo()

