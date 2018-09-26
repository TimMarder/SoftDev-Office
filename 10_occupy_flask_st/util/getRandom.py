from random import randint
from util import getPercent

def theChosenOne():
    theOne = randint(1 , 998)
    ctr = 0                        #counter variable

    for x in getPercent.jobs:
        if theOne < (10 * getPercent.jobs[x] + ctr):
            return x

        ctr += 10 * getPercent.jobs[x]
