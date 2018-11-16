# Tim Marder
# SoftDev1 pd06
# K#26 -- Getting More REST
# 2018-11-16

from flask import Flask, render_template, url_for
import urllib, json, ssl, random

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def api():
    return "<center><h3>Welcome to the API test page!</h3><br><br> \
            Here are the current options of APIs: <br> \
            <a href = " + url_for('gameofthrones') + ">Game of Thrones</a><br> \
            <a href = " + url_for('footballdata') + ">Football Data</a><br> \
            <a href = " + url_for('memegenerator') + ">Meme Generator</a><br>"

@app.route("/gameofthrones")
def gameofthrones():
    url = "https://api.got.show/api/characters/locations"
    context = ssl._create_unverified_context()
    req = urllib.request.urlopen( url , context = context )
    response = req.read()
    data = json.loads( response )
    return render_template("gameofthrones.html",
                           name = data[0]['name'],
                           location = data[0]['locations'])
    #url = "https://api.nasa.gov/planetary/apod?api_key=ueoj9lycxVpsdpUDymbW43EjGxbl2h99DWdatUu3"
    #req = urllib.request.urlopen( url )
    #data = req.read()
    #dictionary = json.loads( data )
    #print(dictionary)
    #return render_template("rest.html",
    #                        img = dictionary[ 'url' ],
    #                        explanation = dictionary[ 'explanation' ])


@app.route("/footballdata")
def footballdata():
    url = "http://api.football-data.org/v2/teams"
    key = "65dfb033ed344dd19156322a63f17a16"
    req = urllib.request.Request( url )
    req.add_header("X-Auth-Token", key)
    response = json.loads( urllib.request.urlopen( req ).read() )
    return render_template("footballdata.html",
                           teams = response['teams'])


@app.route("/memegenerator")
def memegenerator():
    url = "https://memegenerator.net/img/images/"
    rand = random.randint(1,5000)
    key = str( rand ) + ".jpg"
    full_link = url + key
    return render_template("memegenerator.html",
                           img = full_link)


if __name__ == "__main__":
    app.debug = True
    app.run()
