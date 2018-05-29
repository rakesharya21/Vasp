#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:28:28 2018

@author: rakesh
"""
#inserting  selective dynamics before the 8th (index = 7) line
#reading lines from index cnstart onwards after inserting the selective dynamics
cnstart = 9 #usual value is 9 or 10 (note line 10 means cnstart 9)

#define your condition here and add appropriate arguements ro function
def condition():
  return True

#Defining Path to POSCAR
iPOSCARpath = input('Enter path of the input POSCAR file including name of the file ')

#reading POSCAR file from Path
f = open(iPOSCARpath,'r')
lines = f.readlines()

#generating a 2-D list so that each line is a 2-D object 
linlist = []
for i in lines:
    linlist.append(i.split())
f.close()

#Inserting Selective Dynamics Tag, usually added at 7th position change if needed
linlist.insert(7,['Selective Dynamcics'])

for i in range(cnstart, len(linlist)):
    if condition == True: #condition is defined here
        #linlist[i] += ['F','F','F']  #uncomment and add as per your needs
        #linlist[i].append(linlist[i].pop(-4)) #uncomment if element name is written at the end of line
    else:
        #linlist[i] += ['T','T','T'] #uncomment and add as per your needs
        #linlist[i].append(linlist[i].pop(-4)) #uncomment if element name is written at the end of line

#Add more conditions here (Note, the list should look exactly as you want your final POSCAR to look

#Writing the final POSCAR file
oPOSCARpath = input('Enter path of the output POSCAR file including name of the file ')
f = open(oPOSCARpath,'w')

#adds appropriate spaces and formatting
for i in linlist:
    f.write(' '.join(i) + '\n')
    
f.close()