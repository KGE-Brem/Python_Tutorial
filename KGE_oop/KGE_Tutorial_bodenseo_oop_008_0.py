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
    def HoleNamen(self):
        return self.name
    def NeuesBaujahr(self, baujahr):
        self.baujahr = baujahr
    def HoleBaujahr(self):
        return self.baujahr
        

x = Roboter('Marvin', 1979)
y = Roboter('Caliban', 2000)

for rob in [x,y]:     # x, y in eine Liste ablegen siehe auch weiter unten
    rob.SageHallo()
    print('Ich bin ', rob.HoleBaujahr(), ' erschaffen worden')
print() 

# roboter in einer Liste speichern
roboter = []
roboter.append(x)
roboter.append(y)
for rob in roboter:
    rob.SageHallo()
    print(' Baujahr : ', rob.baujahr)
    
