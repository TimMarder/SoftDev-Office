'''
Team Marxians -- Tim Marder & Sophia Xia
SoftDev1 pd6
K6 -- StI/O: Divine your Destiny!
2018-09-13
'''

#import useful function that are used
from csv import reader
from random import randint

jobs = {} #declared an empty dictionary

def getData(): #pulls data from the csv file and adds into dictionary
    file = open('occupations.csv') #opens the csv
    raw = reader(file) #reads the csv
    
    next(file) #skips the first line
    
    for row in raw:
        jobs[row[0]] = float(row[1]) #sets the occupation equal to the
                                     #percentage (float in this case)
    del jobs['Total'] #deletes the last line

#print(jobs) #print function for testing


def theChosenOne(): #chooses an occupation based on weight of occupations
    theOne = randint(1 , 998) #chooses random integer from 1 to 998 
    ctr = 0 #our counter variable
    
    for x in jobs:
        if theOne < (10 * jobs[x] + ctr):
            return x
        
        ctr += 10 * jobs[x]
    '''
    Algo: a randomly chosen number is returned if it smaller than
    the weight of the occupation.
    If it's larger, then the weight of the current occupation is added
    on to the next occupation. This way, the chance of getting a random
    number smaller than the counter increases a little bit each time.
    '''

getData() #executes the getData method
print(theChosenOne()) #executes and prints theChosenOne method




