# Tim Marder
# SoftDev1 pd06
# K#00 -- Bla Bla Bla
# yyyy-mm-dd

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return ""

if __name__ == "__main__":
    app.debug = True
    app.run()
