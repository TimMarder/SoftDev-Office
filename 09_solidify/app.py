# Tim Marder
# SoftDev1 pd06
# K09 -- Solidify
# 2019-09-20

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "<a href='/static/app.html'>No hablo queso!</a>"

if __name__ == "__main__":
    app.debug = True
    app.run()
