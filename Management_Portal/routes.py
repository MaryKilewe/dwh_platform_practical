from Management_Portal import app
from Management_Portal import app
from Management_Portal.forms.forms import PatientRegForm, FilterForm
from datetime import datetime

from flask import Flask
from flask import render_template, url_for, jsonify, flash, request, redirect
import sqlite3
import json
from flask import Blueprint

routes_blueprint = Blueprint('routes_blueprint', __name__,
                                            template_folder='templates',
                                            static_folder='static', static_url_path='/%s' % __name__)


def get_db_connection():
    conn = sqlite3.connect('patient_reg.db')
    conn.row_factory = sqlite3.Row
    return conn

@routes_blueprint.route('/', methods=["GET", "POST"])
@routes_blueprint.route('/index', methods=["GET", "POST"])
def index():
    form  = FilterForm()

    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM patient_registration').fetchall()
    counties = conn.execute('SELECT * FROM counties ORDER BY name ASC').fetchall()
    facilities = conn.execute('SELECT facility FROM patient_registration GROUP BY facility ORDER BY facility ASC').fetchall()
    conn.close()

    form.county.choices = [("", "Show For All")] + [(query[1], query[1]) for query in counties]
    form.facility.choices = [("", "Show For All")] + [(query[0], query[0]) for query in facilities]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    form.month.choices = [("", "Show For All")] + [(month, month) for month in months]
    form.year.choices = [(year, year) for year in range(2020, 2100)]

    return render_template('index.html', form=form)

@routes_blueprint.route('/add_patients', methods=["GET", "POST"])
def add_patients():
    form = PatientRegForm()

    conn = get_db_connection()
    counties = conn.execute('SELECT * FROM counties ORDER BY name').fetchall()
    conn.close()
    form.county.choices = [(query[1], query[1]) for query in counties]

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        gender = form.gender.data
        age = form.age.data
        facility = form.facility.data
        county = form.county.data
        reg_date = form.reg_date.data
        month = reg_date.strftime('%B')
        year = reg_date.strftime('%Y')

        print(month, year)

        conn = get_db_connection()
        conn.execute('INSERT INTO patient_registration (first_name, last_name, gender, age, facility, county, reg_date,reg_month,reg_year) VALUES (?, ?, ?, ?, ?, ?, ?,?,?)',
                     (first_name, last_name, gender, age, facility, county, reg_date, month, year))
        conn.commit()
        conn.close()
        return redirect(url_for('routes_blueprint.submissions'))
    return render_template('add_patients.html', form=form)

@routes_blueprint.route('/submissions', methods=["GET"])
def submissions():
    conn = get_db_connection()
    registrations = conn.execute('SELECT * FROM patient_registration').fetchall()
    conn.close()

    num = 0
    submissions = []
    for row in registrations:
        num +=1
        sub_obj = {}
        sub_obj['number'] = num
        sub_obj['first'] = row[2]
        sub_obj['last'] = row[3]
        sub_obj['gender'] = row[4]
        sub_obj['age'] = row[5]
        sub_obj['facility'] = row[6]
        sub_obj['county'] = row[7]
        sub_obj['reg_date'] = row[8]
        sub_obj['month'] = row[9]
        submissions.append(sub_obj)

    return render_template('submissions.html', submissions=submissions)

@routes_blueprint.route('/<facility>/summary', methods=["GET", "POST"])
def summary(facility):
    conn = get_db_connection()
    facility_summary = conn.execute('SELECT * FROM patient_registration WHERE facility = ?', [facility]).fetchall()
    conn.close()

    num = 0
    summary = []
    for row in facility_summary:
        num += 1
        summ_obj = {}
        summ_obj['number'] = num
        summ_obj['first'] = row[2]
        summ_obj['last'] = row[3]
        summ_obj['gender'] = row[4]
        summ_obj['age'] = row[5]
        summ_obj['facility'] = row[6]
        summ_obj['county'] = row[7]
        summ_obj['reg_date'] = row[8]
        summary.append(summ_obj)

    return render_template('summary.html', facility=facility, summary=summary)

@routes_blueprint.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi')  # Press Ctrl+F8 to toggle the breakpoint.
    return 'hi'