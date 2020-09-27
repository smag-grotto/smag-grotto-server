from flask import Flask, render_template, redirect, request
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Welcome to Smag :)"


@app.route("/users", methods=["GET"])
def users():
    users = requests.get(f"http://{os.getenv('HOST')}:{os.getenv('API_PORT')}/users").json()["users"]

    return render_template("users.html", users=users)


@app.errorhandler(404)
def not_found(e):
    return "Invalid page"


if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=os.getenv("DEBUG"))
