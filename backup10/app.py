# Team ProteinBar -- Tim Marder & Tianrun Liu
# SoftDev1 pd06
# K#10 -- Jinja Tuning
# 2018-09-24

from flask import Flask, render_template
from util import getPercent
from util import getLink
from util import getRandom

#create instance of class Flask
app = Flask(__name__)


#assign fxn to route
@app.route('/')
def home():
    return render_template('home.html');


@app.route('/occupations')
def occupations():
    getPercent.getData()
    getLink.getLinks()
    return render_template( "occupations.html",
                            heading = "Occupations in the U.S.",
                            jobs = jobs,
                            links = links,
                            randomJob = getRandom.theChosenOne()
                            )

if __name__ == "__main__":
    app.debug = True
    app.run()
