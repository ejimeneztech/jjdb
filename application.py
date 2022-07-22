from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Soon, there will be BJJ techniques here :)</p>"
