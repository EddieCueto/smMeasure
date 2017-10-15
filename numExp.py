#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 14:53:22 2017

@author: nlp
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpat

time_vector = open("d_x_times(1-2000,100).txt",'r')  # opens file

timeVect = time_vector.read()  # reads data on file

timeVect = timeVect.replace(" ","")  # this section is to clean the original list
#timeVect = timeVect.replace('',"0")
timeVect = timeVect.replace("\n","")
timeVect = timeVect.replace("[","")
timeVect = timeVect.replace("]","")
#timeVect = timeVect.replace('',"0")

timeVect = timeVect.split(",")   # this line makes a list out of the clean values

timeVect = [float(i)/1000 for i in timeVect]  # this line changes string to float

timeVect = list(filter(lambda a: a != 0.0, timeVect))

#plt.plot(timeVect,'o',ms=0.8)  # plotting the data

cuad = []

for x in range(1,21):
    cuad.append((x**2))
    
plt.plot(cuad,'r')
plt.plot(timeVect)

red_patch = mpat.Patch(color='red', label='x^2')
blue_patch = mpat.Patch(color='blue', label='data')
plt.legend(handles=[red_patch,blue_patch])

plt.ylabel('Time in ms')
plt.xlabel('Group Order*100')

plt.show()