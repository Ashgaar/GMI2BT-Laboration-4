from flask import Flask, request, render_template
import sqlite3
from sqlite3 import Error

database = r"C:\Users\zangi\Programmering\IT-säkerhet Högskolan Dalarna\Skriptprogrammering\Laboration 4\Laboration 4.2\db\weather_data.db3"

app = Flask(__name__)


@app.route('/')
def view_data():
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute('SELECT * FROM weather')
    data = cur.fetchall()
    return render_template("index.html", data=data)


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return conn