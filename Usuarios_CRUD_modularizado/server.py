from flask import Flask, render_template, request, redirect

from flask_app.models.user import User

app = Flask(__name__)

from flask_app.controllers import users
from flask_app import app

if __name__ == "__main__":
    app.run(debug=True)