# Team ProteinBar -- Tim Marder & Tianrun Liu
# SoftDev1 pd06
# K#10 -- Jinja Tuning
# 2018-09-24

from flask import Flask, render_template
from csv import reader
from random import randint

#create instance of class Flask
app = Flask(__name__) 


#assign fxn to route
@app.route('/')
def home():
    return render_template('home.html');

#------------------------------------------------------------------------------

jobs = {}

#pulls the data from the csv file and adds into dictionary
def getData():
    file = open('data/occupations.csv') #opens the csv
    raw = reader(file) #reads the csv

    next(file) #skips the first line

    for row in raw:
        jobs[row[0]] = float(row[1]) #sets the occupation equal to the percentage (float in this case)

    file.close() #close the file when finished


#separate dictionary for the links for each occupation
links = {}

def getLinks():
    file = open('data/occupations.csv')
    raw = reader(file) 

    next(file)

    for row in raw:
        links[row[0]] = str(row[2])


    file.close()


#chooses an occupation based on weight of occupations
def theChosenOne():
    theOne = randint(1 , 998)
    ctr = 0                        #counter variable

    for x in jobs:
        if theOne < (10 * jobs[x] + ctr):
            return x

        ctr += 10 * jobs[x]

@app.route("/occupations")

#print links
def occupations():
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
