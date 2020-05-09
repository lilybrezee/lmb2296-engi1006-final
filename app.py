# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cats")
def cats():
    return render_template("cats.html")

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")

#start the server
if __name__ == "__main__":
    app.run()