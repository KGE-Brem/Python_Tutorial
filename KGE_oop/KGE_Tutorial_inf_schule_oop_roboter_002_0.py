#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
KGE Bremen
2024-07-17

Tutorial https://inf-schule.de/oop/python/roboter
         https://inf-schule.de/oop/python/roboter/objekteklassen
         
"""
# x = rechts,  y = hoch
#     +y  
#     |
#     |
#     +------- +x
#


# Baustein importieren
# import KGE_Tutorial_inf_schule_oop_roboter_001_0 as kge_rob
# Objekt erzeugen
# rob = kge_rob.Roboter()

from KGE_Tutorial_inf_schule_oop_roboter_001_0 import Roboter

rob = Roboter()
# Objekt in Aktion
for i in range(4):
    for j in range(4):
        rob.schritt()
        print(rob.x, rob.y, rob.r)
    rob.links()
    print(rob.x, rob.y, rob.r)