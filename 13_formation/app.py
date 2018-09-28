# Tim Marder
# SoftDev1 pd06
# K#00 -- Bla Bla Bla
# yyyy-mm-dd

from flask import Flask, render_template, request
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return render_template("home.html")

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    print(request.headers)
    return render_template("auth.html",
                            first = request.args['first'],
                            last = request.args['last'],
                            request = request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()
