from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_bcrypt import Bcrypt
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

bcrypt = Bcrypt(app)

DATABASE = "database/users.db"


# ---------------- DATABASE ---------------- #

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

init_db()


# ---------------- HOME ---------------- #

@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")


# ---------------- REGISTER ---------------- #

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"].strip()

        # Input Validation
        if len(username) < 3:
            flash("Username must be at least 3 characters")
            return redirect("/register")

        if len(password) < 6:
            flash("Password must be at least 6 characters")
            return redirect("/register")

        # Hash Password
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()

            # Parameterized Query (SQL Injection Protection)
            cursor.execute(
                "INSERT INTO users(username, password) VALUES(?, ?)",
                (username, hashed_password)
            )

            conn.commit()
            conn.close()

            flash("Registration Successful")
            return redirect("/login")

        except:
            flash("Username already exists")
            return redirect("/register")

    return render_template("register.html")


# ---------------- LOGIN ---------------- #

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"].strip()

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = cursor.fetchone()

        conn.close()

        if user and bcrypt.check_password_hash(user[2], password):

            session["user"] = username
            flash("Login Successful")

            return redirect("/dashboard")

        else:
            flash("Invalid Username or Password")

    return render_template("login.html")


# ---------------- DASHBOARD ---------------- #

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html", user=session["user"])


# ---------------- LOGOUT ---------------- #

@app.route("/logout")
def logout():

    session.pop("user", None)
    flash("Logged Out Successfully")

    return redirect("/login")


# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    app.run(debug=True)
