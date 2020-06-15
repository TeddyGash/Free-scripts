#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 08:16:11 2020

@author: theodore
"""


from datetime import datetime
import time

ai = "Biogbot",
fname = input("Please what is your first name? ")
lname = input("Please what is your last name? ")
gender = input("Are you male or female? ")
if gender.lower() == 'male':
    a = "Mr",
    b = "he",
    c = "He",
    d = "boy",
    e = "handsome",
    f = "his",
    g = "man",
elif gender.lower() == 'female':
    a = "Ms",
    b = "she",
    c = "She",
    d = "girl",
    e = "pretty",
    f = "her",
    g = "lady",
else:
    g ="not specified",
dob = input("Enter DOB, use dd/mm/yyyy format: ")
dob = datetime.strptime(dob, '%d/%m/%Y')
favfood = input ("What is your favorite food? ")
residence = input ("Where do you live? ")

time.sleep(2)
print("\n\nHello %s"  % (a), fname, "my name is %s" % (ai),) 
time.sleep(3)
#I am your Personal Assistant and have a story for you (THE NAME OF THE USER).
print("I am your Personal Assistant and have a story for you, %s" % (fname),)
time.sleep(4)
print("Sit back and enjoy.\n\n") 
time.sleep(6)
print("In the year %s" % (dob.year), "the %s" % (lname), "family gave birth to a beautiful baby %s" % (d),
 "called %s" % (fname),".")
time.sleep(6)
print("%s" % (fname), "was so cute and grew to be a %s" % (e), "young %s" % (g),)
time.sleep(6)
print("%s" % (c), "loves %s" % (favfood), "and currently lives in %s" % (residence),".")
time.sleep(8)
print("%s" % (c), "thinks I don't know that %s" % (b), "is %d" % ((datetime.today() - dob).days/365), 
"years, but by only providing %s" %(f), "date of birth I can get that 😉.")
time.sleep(8)
print("All I needed were few calculations and tah da!")
time.sleep(9)
print("And in case you are wondering, %s" % (f), " full name is %s" % (a), (fname), (lname),)
time.sleep(9)
print("\nWell thanks so much for your time, looking forward to getting to know you better 😊")
time.sleep(8)
print("\nBye,\n\n%s" % (ai),)
print ("---------------------------------")