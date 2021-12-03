from flask import Flask
from flask import render_template, url_for, jsonify, redirect
import sqlite3
import json

from Management_Portal import app

'''
# Initialise the Flask App
app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('patient_reg.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=["GET", "POST"])
def home():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM patient_registration').fetchall()
    conn.close()

    data = []
    for row in posts:
        data.append([x for x in row])
    return json.dumps(data)

@app.route('/submissions', methods=["GET", "POST"])
def submissions():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi')  # Press Ctrl+F8 to toggle the breakpoint.
    return 'hi'

@app.route('/facility/summary', methods=["GET", "POST"])
def summary():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi')  # Press Ctrl+F8 to toggle the breakpoint.
    return 'hi'

@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi')  # Press Ctrl+F8 to toggle the breakpoint.
    return 'hi'''

if __name__ == "__main__":

    app.run(debug=True)
