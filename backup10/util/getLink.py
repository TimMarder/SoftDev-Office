from csv import reader

links = {}

def getLinks():
    file = open('data/occupations.csv')
    raw = reader(file)

    next(file)

    for row in raw:
        links[row[0]] = str(row[2])

    file.close()
