from flask import Flask, render_template, request, redirect
import sqlite3
import qrcode
import os

app = Flask(__name__)

# create database table
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS qr_codes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE,
        target_url TEXT,
        scans INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()

init_db()


# dashboard
@app.route("/")
def dashboard():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM qr_codes")
    data = cursor.fetchall()

    conn.close()

    return render_template("dashboard.html", qr_codes=data)


# create qr
@app.route("/create", methods=["GET","POST"])
def create():

    if request.method == "POST":

        code = request.form["code"]
        url = request.form["url"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO qr_codes(code,target_url) VALUES (?,?)",
            (code,url)
        )

        conn.commit()
        conn.close()

        qr_link = f"http://localhost:8080/q/{code}"

        img = qrcode.make(qr_link)
        img.save(f"static/qr/{code}.png")

        return redirect("/")

    return render_template("create.html")


# redirect + count scans
@app.route("/q/<code>")
def qr_redirect(code):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT target_url FROM qr_codes WHERE code=?", (code,))
    result = cursor.fetchone()
    print(result)
    if result:

        cursor.execute(
            "UPDATE qr_codes SET scans = scans + 1 WHERE code=?",
            (code,)
        )

        conn.commit()
        conn.close()

        return redirect(result[0])

    print("QR not found")
    return "QR not found"


app.run(port=8080,debug=True)