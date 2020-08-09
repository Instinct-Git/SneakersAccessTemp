from flask import Flask, render_template, request
from flaskwebgui import FlaskUI

app = Flask(__name__)
ui = FlaskUI(app)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
    else:
        return render_template('index.html')


@app.route("/profiles")
def profiles():
    return render_template('profiles.html')


@app.route("/captcha")
def captcha():
    return render_template('captcha.html')


if __name__ == "__main__":
    ui.run()
