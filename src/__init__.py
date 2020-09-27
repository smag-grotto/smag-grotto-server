from flask import Flask, render_template, redirect, request, url_for
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/leaderboard", methods=["GET"])
def leaderboard():
    return render_template("leaderboard.html")


@app.route("/members", methods=["GET"])
def members():
    members = requests.get(f"http://{os.getenv('API_HOST')}:{os.getenv('API_PORT')}/members").json()["members"]

    return render_template("members.html", members=members)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=os.getenv("DEBUG"))
