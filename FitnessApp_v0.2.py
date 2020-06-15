#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 08:26:21 2020

@author: theodore
"""
class Client:  
    def receiveName(self):
        name = input("Please enter your name: ").upper()
        self.name= name

    def receiveAge(self):
        age = int(input("Please enter your age: "))
        self.age= age

    def receiveWeight(self):
        weight= float (input('Please your current weight (in kg): '))
        self.weight=weight

    def receiveHeight(self): 
        height = float (input("Please enter your height (in metres): "))
        self.height = height
    

    def calcBMI (self):
        bmi = self.weight/pow(self.height, 2)
        self.bmi = bmi

    def askNameconfirmation(self):
        confirmation = input (self.name + ", right? y/n ").lower()
        self.confirmation = confirmation
        

    def reEntername(self):
        reenteredname = input("Please re-enter your name: ")
        self.name = reenteredname


    def confirmName(self):
        if self.confirmation[0]=='y':
            pass
        else:
            self.retakeName()
            
    def retakeName(self):
        while self.confirmation != 'y':
                self.reEntername()
                self.askNameconfirmation()

    def welcome_client(self):
        print ("Hey " + self.name + "! Welcome to today's exercise session." )

    def verifyHeight (self):
        if 0.5 < self.height < 2:
            pass
        else:
            self.reEnterheight()

    def reEnterheight (self):
        while self.height < 0.5 or self.height > 2:
            reenteredheight = float (input("Please make sure your height is in metres: "))
            self.height = reenteredheight

    def verifyWeight(self):
        if 10 < self.weight < 250:
            pass
        else:
            self.reEnterweight()

    def reEnterweight(self):
        while self.weight < 10 or self.weight > 250:
            reenteredweight= float (input("Please make sure your weight is in kg: "))
            self.weight = reenteredweight

    def receiveInput(self):
        self.receiveName()
        self.askNameconfirmation()
        self.confirmName()
        self.receiveAge()
        self.receiveWeight()
        self.verifyWeight()
        self.receiveHeight()
        self.verifyHeight()


    def comment_bmi(self):
        if 18< self.bmi <25:
            self.comment_good()
        elif self.bmi < 18:
            self.comment_underweight()
        else:
            self.comment_overweight()


    def comment_good(self):
        print ("Congratulations, " + self.name.title() + "! You're in good shape! %0.2f" %(self.bmi) + " is within the recommended\n range of 18.00-25.00kg/m2.")

    def comment_underweight(self):
        print ("That does not look good, " + self.name.title() + ". %0.2f" %(self.bmi) + " is below the recommended\n range of 18.00-25.00kg/m2." )

    def comment_overweight(self):
        print ("That does not look good, " + self.name.title() + ". %0.2f" %(self.bmi) + " is above the recommended\n range of 18.00-25.00kg/m2.")


    
    def recommendedWeight_max(self):
        recommendedweight_max = pow(self.height, 2) * 25
        self.recommendedweight_max = recommendedweight_max
        return self.recommendedweight_max

    
    def recommendedWeight_min(self):
        recommendedweight_min = pow(self.height, 2) * 18
        self.recommendedweight_min = recommendedweight_min
        return self.recommendedweight_min

    def recommendWeight4height(self):
        print("The recommended weight range for your height is: %0.2f " %(self.recommendedweight_min) + "to %0.2f" %(self.recommendedweight_max) + "kg.")

    def calcWeighttolose(self):
        if self.bmi > 25:
            weighttolose= self.weight - (pow(self.height, 2) * 23)
            self.weighttolose = weighttolose
            return self.weighttolose

    def calcWeighttogain(self):
        if self.bmi < 18:
            weighttogain = (pow(self.height, 2) * 23) - self.weight
            self.weighttogain = weighttogain
            return self.weighttogain
        
    def calcWeightto_gl(self):
        self.calcWeighttogain()
        self.calcWeighttolose()

    def commentWeightto_gl(self):
        if self.bmi > 25:
            print("Based on your current weight, you'll need to lose %0.2f" %(self.weighttolose) + "kg \nin order to fall back into the recommended BMI range.")

        elif self.bmi < 18:
            print("Based on your current weight, you'll need to gain %0.2f" %(self.weighttogain) + "kg \nin order to fall back into the recommended BMI range.")
    
    def giveAssurance(self):
        if self.bmi < 18 or self.bmi > 25:
            print("But don't be worried, we'll be glad to help you through it.")
            
    def space(self):
        print("")
        
    def report(self):
        self.header()
        self.body()
        self.footer()


    def header(self):
        print("\n\n                 REPORT: " + self.name)
        print("============================================================")


    def body(self):
        print("Hey, " + (self.name).title() + "! \nThis is your fitness report for today: ")
        print("\t Height........................................" + str(self.height) + "m.")
        print("\t Current Weight................................" + str(self.weight) + "kg.")
        print("\t BMI..........................................." + str("%0.2f" %(self.bmi)) + "kg/m2.")
        print("                 ****Comments****")
        self.comment_bmi()
        self.space()
        self.commentWeightto_gl()
        self.space()
        self.giveAssurance()


    def footer(self):
        print("============================================================")
        print("                 ****Stay fit!****")


    def run(self):
        self.receiveInput()
        self.calcBMI()
        self.calcWeightto_gl()
        self.report()

client1 = Client().run()

