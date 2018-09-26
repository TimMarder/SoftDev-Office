from csv import reader

jobs = {}

#pulls the data from the csv file and adds into dictionary
def getData():
    file = open('data/occupations.csv') #opens the csv
    raw = reader(file) #reads the csv

    next(file) #skips the first line

    for row in raw:
        jobs[row[0]] = float(row[1]) #sets the occupation equal to the percentage (float in this case)

    file.close() #close the file when finished

    return jobs
