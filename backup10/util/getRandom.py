from random import randint

def theChosenOne():
    theOne = randint(1 , 998)
    ctr = 0                        #counter variable

    for x in jobs:
        if theOne < (10 * jobs[x] + ctr):
            return x

        ctr += 10 * jobs[x]
