# -*- coding: utf-8 -*-
"""


"""
import os
import sys

from flask import Flask, render_template, json, request
from flask import flash, redirect, session, abort




app = Flask(__name__)
app.debug = True
###function that reads json files 

@app.route("/")
def index():
    return "OK"
         

if __name__ == "__main__":
    app.run()
    #app.run(host='10.108.161.123', port=5000)
