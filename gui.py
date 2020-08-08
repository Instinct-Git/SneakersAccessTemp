import os
from flask import Flask, render_template, request
from flaskwebgui import FlaskUI

app = Flask(__name__)
ui = FlaskUI(app)

@app.route("/")
def index():
    return render_template('index.html')

ui.run()