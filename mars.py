# This is a riddle about surviving on mars.
# Your goal is to survive for 1,825 earth days, or about 5 years.
# You have critical life support infrastructure, as well as 3 3D printers to aid you in making parts required to ensure your survival.

# One part of your critical life support infrastructure will break every day, and require a replacement part made by one of your printers.
# Your 3D printers are made by different manufacturers, and thus you are unable to scavenge them for parts interchangeably. You can however, print
# the required parts for repair.
# Each printer is capable of creating 1 part per day.
# Sometimes, the printers break. Thance that each of the three printers break on a given day are: 10% for p1, 7.5% for p2, 5% for p3self.

# What is the probability that you will survivie for 1825 days?

import random
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


#Probablilities

p1break = 0.1
p2break = 0.075
p3break = 0.05

iterations = 10000

#One day
def survive():

    #Printer status
    status = [1,1,1]
    #Probabilities out of 1000 to use integers
    probs = [p1break*1000, p2break*1000, p3break*1000]
    days = 0


    while True:

        #Check machine status on given day, if working
        for idx,val in enumerate(status):
            if val == 1:
                if (random.randint(1,2500) <= probs[idx]):
                    status[idx] = 0

        #If machine is broken, test if it can be fixed
        for idx,val in enumerate(status):
            if val == 0:

            #Count how many of the other machines are working
                working = 0
                for x in status:
                    working = working + x
                #No machines working, you' dead sucka
                if working == 0:
                    return days
                #2 Machines working, you can be fixed!
                if working == 2:
                    status[idx] = 1
        days = days + 1






#This block runs survive() multiple times and tallies the results

count = 0
avgdays = 0
survival = 0
days = []


while(count < iterations):
    surviveddays = survive()
    avgdays = avgdays + surviveddays
    days.append(surviveddays)
    count = count + 1
    if surviveddays >= 1825:
        survival = survival + 1
print ("You survived on average %s days after %s iterations" % ((avgdays/iterations),(iterations)))
print ("Number of times survived = %s" % survival)
print ("Your survival probability is %s%%" % ((survival/iterations)*100))






#Plotting a simple histogram

sigma = np.std(days)
num_bins = 50
fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(days, num_bins, density=1)

# add a 'best fit' line
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - avgdays))**2))
ax.plot(bins, y, '--')
ax.set_xlabel('Days Survived')
ax.set_ylabel('Probability density')
ax.set_title('Histogram of Days survived on Mars')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
