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


class Roboter(object):
    def __init__(self, x=0, y=0, r='O'):
        self.x = x
        self.y = y
        self.r = r

    def schritt(self):
        if self.r == 'O':
            self.x = self.x + 1
        elif self.r == 'S':
            self.y = self.y - 1
        elif self.r == 'W':
            self.x = self.x - 1
        elif self.r == 'N':
            self.y = self.y + 1

    def rechts(self):
        if self.r == 'O':
            self.r = 'S'
        elif self.r == 'S':
            self.r = 'W'
        elif self.r == 'W':
            self.r = 'N'
        elif self.r == 'N':
            self.r = 'O'

    def links(self):
        if self.r == 'O':
            self.r = 'N'
        elif self.r == 'N':
            self.r = 'W'
        elif self.r == 'W':
            self.r = 'S'
        elif self.r == 'S':
            self.r = 'O'

#rob_01 = Roboter(5,5, 'S')
#rob_02 = Roboter(10, 10, 'W')


#print('rob_01 ', rob_01.__dict__)
#print('rob_02 ', rob_02.__dict__)
