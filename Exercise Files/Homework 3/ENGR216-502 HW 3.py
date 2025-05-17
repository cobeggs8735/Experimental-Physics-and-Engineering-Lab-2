#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:52:15 2019

@author: colemanbeggs
"""

# Coleman Beggs
# ENGR216-502
# 1 October 2019

import numpy as np
import csv
import matplotlib.pyplot as plt
import statistics
from scipy.stats import norm


# 1 a)
with open ("PatientTemperature_CSV.csv") as PatientTempFile:
    PatTemp = csv.reader(PatientTempFile, delimiter = ",")
    temp = []
    age = []
    for i in PatTemp:
        temp.append(float(i[0]))
        age.append(float(i[1]))
    print ("Read file into Program")
    
    # 1 b)
    meanTemp = 0
    for x in temp:
        meanTemp += x
    meanTemp /= len(temp)
    
    modeTemp = statistics.mode(temp)
    varTemp = statistics.variance(temp)
    stdTemp = statistics.stdev(temp)
    medTemp = statistics.median(temp)
    print("1 b)\n", "Mean temp is:", meanTemp, "\n", "Mode temp is:", modeTemp, "\n", "Variance in temp is:", varTemp, "\n", "Standard Deviation of temp is:", stdTemp, "\n", "Median temp is:", medTemp, "\n")
    
    
    # 1 c)
    meanAge = 0
    for n in age:
        meanAge += n
    meanAge /= len(age)
    
    #modeAge = statistics.mode(age)
    """
    After filtering the data in excel to ascending order, then counting the number of times each sample occurs,
    the two values for the mode are 73 and 78
    """
    varAge = statistics.variance(age)
    stdAge = statistics.stdev(age)
    medAge = statistics.median(age)
    print("1 c)\n","Mean age is:", meanAge, "\n", "Mode age is 73 and 78\n",  "Variance of age is:", varAge, "\n", "Standard Deviation of age is:", stdAge,"\n", "Median age is:", medAge, "\n")
        
    # 1 d)
    #print("1 d)")
    plt.hist(temp, facecolor = "blue")
    plt.xlabel("Patient Temperature")
    plt.ylabel("Frequency")
    plt.title("1 d)")

plt.hist(temp, facecolor = "blue")
plt.xlabel("Patient Temperature")
plt.ylabel("Frequency")
plt.title("1 d)")

#rnge = np.arange(-3, 3, .01)
#plt.plot(rnge, norm.pdf(rnge, 0, 1))

def draw_z_score(x, cond, mu, sigma, title):
    y = norm.pdf(x, mu, sigma)
    z = x[cond]
    plt.plot(x, y)
    plt.fill_between(z, 0, norm.pdf(z, mu, sigma))
    plt.title(title)
    plt.show()

plt.hist(temp, facecolor = "blue")
plt.xlabel("Patient Temperature")
plt.ylabel("Frequency")
plt.title("1 d)")

# 2
avg = 100
stdev = 5
N = 1
iq = 110
z1 = (iq - avg)/stdev
z2 = z1 + .5 # From z-table
prob = 1 - z2
print("2\n", "Probability of iq over 110 is:", prob*100, "%\n")
x = np.arange(0, 200, .01)
draw_z_score(x, x > iq, avg, stdev, "Bell Curve #2")

# 3 
avg = 16
stdev = 2
ovrFill = 18
z3 = (ovrFill - avg)/stdev
z4 = z3 + 0.5 # From z-table
prob = 1 - z4
x = np.arange(0, 32, .01)
print("3\n", "Probability cup overfilled (more than 18 oz)", prob*100, "%\n")
draw_z_score(x, x > ovrFill, avg, stdev, "Bell Curve #3")

# 4
avgTime = 4000
stdev = 200
z5 = 2.054
prct = 2
lifeTime = avgTime-z5*stdev
x = np.arange(0, 8000, .01)
print("4\n", "Company should promote a lifetime of:", lifeTime, "hours\n")
draw_z_score(x, x < lifeTime, avgTime, stdev, "Bell Curve #4")

# 5 
avgTime = 10
stdev = 2
prct = 3
z6 = 1.88 # From z-table
lifeTime = avgTime-z6*stdev
x = np.arange(0, 20, .01)
print("5\n", "Company should gaurantee", lifeTime, "years\n")
draw_z_score(x, x < lifeTime, avgTime, stdev, "Bell Curve #5")

plt.hist(temp, facecolor = "blue")
plt.xlabel("Patient Temperature")
plt.ylabel("Frequency")
plt.title("1 d)")
