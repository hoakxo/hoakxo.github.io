import os
import datetime
import sqlite3 as sql
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

# configuring app
app = Flask(__name__)

# ensuring templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# configuring session to use filesystem (instead of signed in cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# importing user database
db = mysql.connector.connect()
def get_db():
    try:
        connection = sql.connect("user_database.db", uri=True)
        connection.row_factory = sql.Row
    except:
        print("Error opening database, please check file exists in correct directory.")
        os.sys.exit(1)
    return connection


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.header["Expires"] = 0
    response.header["Pragma"] = "no-cache"
    return response


# @app.route("/")
# @login_required
# def index():


@app.route("/")
def home():
    return "Hello app"

# PROGRESS

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "GET":
        return render_template("register.html")
    
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return ("Please enter username.")

# APP PROGRESS
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return ("must provide username", 403)
        
        # Ensure password was submitted
        elif not request.form.get("password"):
            return ("must provide password", 403)
        
        # Query database for username
        rows = db