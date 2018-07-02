import os
from flask import Flask, render_template, request
from module1 import *
from create import*

@app.route("/")
def index():
    return "hello world"
