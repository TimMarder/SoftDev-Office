# Team ProteinBar -- Tim Marder & Tianrun Liu
# SoftDev1 pd06
# K#10 -- Jinja Tuning
# 2018-09-24

from flask import Flask, render_template
from csv import reader
from random import randint

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "<title> Team ProteinBar's Website </title> \
    <center><h1> Team ProteinBar // SoftDev1 pd06</h1> \
    <h3>Tim Marder & Tianrun Liu</h3> \
    Yo hablo queso! <br> \
    Welcome to our website! <br> \
    <b>Click <a href = '/occupations'>here</a> for occupations!</b></center>"

#------------------------------------------------------------------------------

jobs = {}

def getData(): #pulls data from the csv file and adds into dictionary
    file = open('data/occupations.csv') #opens the csv
    raw = reader(file) #reads the csv

    next(file) #skips the first line

    for row in raw:
        jobs[row[0]] = float(row[1]) #sets the occupation equal to the
                                     #percentage (float in this case)

    del jobs['Total'] #deletes the last line

    file.close() #close the file when finished

links = {} #separate dictionary for the links for each occupation

def getLinks(): #pulls data from the csv file and adds into dictionary
    file = open('data/occupations.csv') #opens the csv
    raw = reader(file) #reads the csv

    next(file) #skips the first line

    for row in raw:
        links[row[0]] = str(row[2])

    del links['Total'] #deletes the last line

    file.close() #close the file when finished

def theChosenOne(): #chooses an occupation based on weight of occupations
    theOne = randint(1 , 998) #chooses random integer from 1 to 998
    ctr = 0 #our counter variable

    for x in jobs:
        if theOne < (10 * jobs[x] + ctr):
            return x

        ctr += 10 * jobs[x]

@app.route("/occupations")
def occupations():
    #print(links) #for testing
    getData()
    getLinks()
    return render_template( "occupations.html",
                            heading = "Occupations in the U.S.",
                            jobs = jobs,
                            links = links,
                            randomJob = theChosenOne()
                            )

if __name__ == "__main__":
    app.debug = True
    app.run()
