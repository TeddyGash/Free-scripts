#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 08:10:35 2020

@author: theodore
"""


print('Welcome to Theodore\'s Interest Calculator')
amount = float(input('\nPrincipal amount?'))
currency = input ('Currency (use symbol)')
roi = float(input('Rate of Interest?'))
years = int(input('Duration (no. of years)?'))
total = (amount * pow(1 + (roi/100), years))
interest = total - amount
print("\n Interest =",currency,"%0.2f" % interest )
print("\n You'll therefore pay a total of= %s" % currency, "%0.2f" % (total))