# Tim Marder
# SoftDev1 pd06
# K#08 -- Fill Yer Flask
# 2018-09-20

from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route("/")
def hello_world():
    #print("about to print __name__...")
    #print(__name__)
    return "No hablo queso! <br> For welcome page click <a href = " + url_for("welcome") + ">here</a> <br> For bio page click <a href = " + url_for("about_me") + ">here</a>"

@app.route("/welcome")
def welcome():
    return "Welcome to my website! Hope you enjoy the contents! <br> Return to the home page <a href = " + url_for("hello_world") + ">here</a>"

@app.route("/bio")
def about_me():
    return "My name is Tim. I take Software Development. Nice to meet you! <br> Return to the home page <a href = " + url_for("hello_world") + ">here</a>"

if __name__ == "__main__":
    app.debug = False #Make sure to turn off when done!
    app.run()
