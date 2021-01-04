# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:06:33 2021

@author: MM
"""
import webbrowser
from time import sleep
from re import sub
tekst=(input('Podaj Tekst: ').lower().replace(" ",""))
tekst=sub("[^a-z łęóąśżźćń]", "", tekst)
print (tekst[::-1])

if tekst==tekst[::-1]: 
    print('To wyrażenie jest palindromem')
    sleep(2)
    website = "https://poocoo.pl/scrabble-slowa-z-liter/" + tekst
    webbrowser.open(website)
else:
    print('To wyrażenie nie jest palindromem')

