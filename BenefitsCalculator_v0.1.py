#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 08:06:43 2020

@author: theodore
"""


#Create Worker attributes
class Worker:
    
    def setName (self, name):
        name = name.upper()
        self.name = name
        
    def getName (self):
        return self.name
    
    #Employment duration
    def setEmpDur (self, emp_dur):
        emp_dur = int(emp_dur)
        self.emp_dur = emp_dur
        
    def getEmpDur (self):
        return emp_dur
    
    #Worker's rank
    def setRank (self, rank):
        rank = rank.lower()
        self.rank = rank
        
    def getRank (self):
        return rank
    
    #Worker's Basic salary
    def setBasic_salary (self, basic_salary):
        self.basic_salary = float (basic_salary)
        
    def getBasic_salary (self):
        return basic_salary
    
    def setDur_benefit(self):
         #benefit based on duration of employment
        #def calc_dur_benefit (self, emp_dur):
            if self.emp_dur > 10:
                self.dur_benefit = ((10/100) * self.basic_salary)
            elif 5 < self.emp_dur < 10:
                self.dur_benefit = ((5/100) * self.basic_salary)
            else:
                self.dur_benefit = ((2/100) * self.basic_salary)
            #return dur_benefit
        
    def getDur_benefit(self):
        return dur_benefit
    
    def setRank_benefit(self):
         #benefit based on rank
        #def calc_rank_benefit (self, rank):
        if self.rank == "senior":
            self.rank_benefit = ((5/100) * self.basic_salary)
            
        elif self.rank == "middle":
            self.rank_benefit = ((3/100) * self.basic_salary)
            
        elif self.rank == "lower":
            self.rank_benefit = ((1/100) * self.basic_salary)
            
        #return rank_benefit
    
    
    def getRank_benefit(self):
        return rank_benefit
    
    
    def setGross_benefit(self):
         #the Gross benefit
        #def calc_gross (self, basic_salary, dur_benefit, rank_benefit):
        self.gross_benefit = (self.basic_salary + self.dur_benefit + self.rank_benefit + self.life_benefit)
        #return gross_benefit

    def getGross_benefit(self):
        return gross_benefit
    
    #Constant Life benefit for all workers
    def setLife_benefit (self):
        self.life_benefit = ((2/100) * self.basic_salary)
    
    def getLife_benefit(self):
        return life_benefit
    
    #calculation of various benefits
#class Benefit_calculation (Worker):
   
    
   
    
   
    #print (self.name\n\n "\t Gross salary is GHc" gross_benefit )
    
    
    def generate_benefits (self):
        print ("WELCOME TO THEODORE'S BENEFITS CALCULATOR")

        name = input ("\nEnter Employee's name: ")
        emp_dur = input ("Enter Employee's duration of employment (in years): ")
        rank = input ("Enter Employee's rank (senior/middle/lower): ")
        basic_salary = input ("Enter Employee's Basic salary: ")

        self.setName(name)
        self.setEmpDur(emp_dur)
        self.setRank(rank)
        self.setBasic_salary(basic_salary)
        self.setDur_benefit()
        self.setRank_benefit()
        self.setLife_benefit()
        self.setGross_benefit()

        print ("\n      \t\tBENEFITS: ", name.upper() )
        print ("____________________________________________________")
        print ("\t Employment Duration Benefit: GHc ", self.dur_benefit)
        print ("\t Rank Benefit:                GHc ", self.rank_benefit)
        print ("\t Life Benefit:                GHc ", self.life_benefit)
        print ("\t Basic Salary:                GHc ", self.basic_salary)
        print ("_____________________________________________________")
        print ("\t GROSS BENEFITS:              GHc", self.gross_benefit)

        
        
worker1 = Worker().generate_benefits()



        
