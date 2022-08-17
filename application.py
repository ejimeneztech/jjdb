from email.mime import application
from flask import Flask, render_template
import requests
from aws_requests_auth.aws_auth import AWSRequestsAuth
import os

app = Flask(__name__)



GET_POSTS = "https://7shbjqoi1m.execute-api.us-west-2.amazonaws.com/dev/jitzdb-get-posts"
GET_DETAIL = "https://7shbjqoi1m.execute-api.us-west-2.amazonaws.com/dev/jitzdb-get-detail"


ACCESS_KEY = os.environ["AWS_ACCESS_KEY_ID"]
SECRET_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]



auth = AWSRequestsAuth(aws_access_key=ACCESS_KEY,
                       aws_secret_access_key=SECRET_KEY,
                       aws_host='c0v0uykzq5.execute-api.us-west-2.amazonaws.com',
                       aws_region='us-west-2',
                       aws_service='execute-api')


@app.route("/")
def home():
    response = requests.get(GET_POSTS)
    response.raise_for_status()
    data = response.json()
    posts = data["body"]["Items"]
    return render_template('home.html', posts=posts)


@app.route("/detail/<postId>")
def detail(postId):
    response = requests.post(GET_DETAIL, json={"id": f"{postId}"}, auth=auth)
    response.raise_for_status()
    data = response.json()
    details = data["body"]["Item"]
    return render_template('detail.html', postId=postId, details=details)
    