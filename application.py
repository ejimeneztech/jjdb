from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route("/detail")
def detail():
    return render_template('detail.html')