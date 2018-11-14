# Tim Marder
# SoftDev1 pd06
# K#23 -- A RESTful Journey Skyward
# 2018-11-13

from flask import Flask, render_template
import urllib, json

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def api():
    url = "https://api.nasa.gov/planetary/apod?api_key=ueoj9lycxVpsdpUDymbW43EjGxbl2h99DWdatUu3"
    req = urllib.request.urlopen( url )
    data = req.read()
    dictionary = json.loads( data )
    #print(dictionary)
    return render_template("rest.html",
                            img = dictionary[ 'url' ],
                            explanation = dictionary[ 'explanation' ])

if __name__ == "__main__":
    app.debug = True
    app.run()
