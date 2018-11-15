# Tim Marder
# SoftDev1 pd06
# K#25 -- Getting More REST
# 2018-11-15

from flask import Flask, render_template
import urllib, json

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def api():
    #req = urllib.request.urlopen('https://api.fullcontact.com/v3/person.enrich')
    #req.add_header('Authorization', 'Bearer tDIoCN29nofEdUHQiqsIb9NbvOwIDad4')
    #data = req.read()
    req = urllib.request.Request('https://api.fullcontact.com/v3/person.enrich')
    req.add_header('Authorization', 'Bearer tDIoCN29nofEdUHQiqsIb9NbvOwIDad4')
    response = urllib.request.urlopen(req)
    dictionary = json.loads( data )
    return dictionary
    return render_template("rest.html",
                            img = dictionary[ 'url' ],
                            explanation = dictionary[ 'explanation' ])

if __name__ == "__main__":
    app.debug = True
    app.run()
