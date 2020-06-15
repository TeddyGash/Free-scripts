#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 08:00:36 2020

@author: theodore
"""


doctor = input ('Please enter your name')
patient = input ('Patient\'s full name').upper ()
drug = input ('Name of drug').upper()
dosage = input ('Dosage')
freq = input ('How many times in a day?')
duration = input ('For how long?')

print ('\n%s:' % patient, '%s' % drug, '\n...........................')
print ("\nTake %s" %dosage, "%s" % freq, "time(s) daily for %s" % duration, "day(s). Do come back when you run out.\nThank you.\n\nDr. %s" % doctor, "\n...........")