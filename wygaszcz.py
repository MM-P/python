# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 11:53:05 2020

@author: abc
"""

from turtle import *

from random import randint 

speed(0)

bgcolor('black')

x = 1
hideturtle()
while x < 9000:
    r = randint(0,255) 
    g = randint(0,255) 
    b = randint(0,255) 
    colormode(255) 
    pencolor(r,g,b) 
    fd(50 + x)
    rt(90.911)
    x = x+1 

exitonclick() 

