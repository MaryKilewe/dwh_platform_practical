

from Management_Portal.forms.forms import PatientRegForm
from .filter_charts import *
from datetime import datetime
from flask import Flask
from flask import render_template, url_for, jsonify, flash, request, redirect
import sqlite3
import json
from flask import Blueprint

statistics_blueprint = Blueprint('statistics_blueprint', __name__,
                                            template_folder='../templates',
                                            static_folder='../static', static_url_path='/%s' % __name__)


def get_db_connection():
    conn = sqlite3.connect('patient_reg.db')
    conn.row_factory = sqlite3.Row
    return conn

@statistics_blueprint.route("/get_gender_statistics", methods=["GET"])
def get_gender_statistics():
    # this route returns the genders of candidates

    conn = get_db_connection()
    gender_stats = conn.execute('SELECT gender, COUNT(*) FROM patient_registration GROUP BY gender').fetchall()
    conn.close()

    # format query results for the chart
    genders_stats = []
    for gender_data in gender_stats:
        genders_stats.append((gender_data[0], gender_data[1]))

    return jsonify(genders_stats)


@statistics_blueprint.route('/gender_filter', methods=['POST'])
def gender_filter():
    month = request.get_json()['month'] if request.get_json()['month'] != '' else None
    year = request.get_json()['year'] if request.get_json()['year'] != '' else None
    facility = request.get_json()['facility'] if request.get_json()['facility'] != '' else None
    county = request.get_json()['county'] if request.get_json()['county'] != '' else None

    filtered_genders = filter_genders(month, year, facility, county)

    return jsonify(filtered_genders)


@statistics_blueprint.route("/get_age_statistics", methods=["GET"])
def get_age_statistics():
    # this route returns the age ranges of patients

    conn = get_db_connection()
    age_stats = conn.execute('SELECT id, age FROM patient_registration').fetchall()
    conn.close()

    # format query results for the chart
    ages = []
    for gender_data in age_stats:
        ages.append(gender_data[1])

    grouped_ages = [('0 - 9', count_range_in_list(ages, 0, 9)),
                             ('10 - 19', count_range_in_list(ages, 10, 19)),
                             ('20 - 29', count_range_in_list(ages, 20, 29)),
                             ('30 - 39', count_range_in_list(ages, 30, 39)),
                             ('40 - 49', count_range_in_list(ages, 40, 49)),
                             ('50 - 59', count_range_in_list(ages, 50, 59)),
                             ('60 - 69', count_range_in_list(ages, 60, 69)),
                             ('70 - 79', count_range_in_list(ages, 70, 79)),
                             ('80 - 89', count_range_in_list(ages, 80, 89)),
                             ('90 - 99', count_range_in_list(ages, 90, 99)),
                             ('100 - 109', count_range_in_list(ages, 100, 109)),
                             ('110 - 120', count_range_in_list(ages, 110, 120)),
                             ]

    return jsonify(grouped_ages)

def count_range_in_list(li, min, max):
    ctr = 0
    for x in li:
        if min <= x <= max:
            ctr += 1
    return ctr


@statistics_blueprint.route('/age_filter', methods=['POST'])
def age_filter():
    month = request.get_json()['month'] if request.get_json()['month'] != '' else None
    year = request.get_json()['year'] if request.get_json()['year'] != '' else None
    facility = request.get_json()['facility'] if request.get_json()['facility'] != '' else None
    county = request.get_json()['county'] if request.get_json()['county'] != '' else None

    filtered_ages = filter_ages(month, year, facility, county)
    print(filtered_ages)
    return jsonify(filtered_ages)


@statistics_blueprint.route("/monthly_reg_stats", methods=["GET"])
def monthly_reg_stats():
    # this route returns monthly registrations

    conn = get_db_connection()
    reg_stats = conn.execute('SELECT reg_month, COUNT(*) FROM patient_registration WHERE reg_year = "2021" GROUP BY reg_month').fetchall()
    conn.close()

    # format query results for the chart
    monthly_reg = {}
    for reg_data in reg_stats:
        monthly_reg[reg_data[0]] = reg_data[1]

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    grouped_registrations = []
    for month in months:
        if month in monthly_reg:
            grouped_registrations.append((month, monthly_reg[month]))
        else:
            grouped_registrations.append((month, 0))
    '''filtered_grouped_ages = [('January', count_range_in_list(ages, 0, 9)),
                             ('February', count_range_in_list(ages, 10, 19)),
                             ('March', count_range_in_list(ages, 20, 29)),
                             ('April', count_range_in_list(ages, 30, 39)),
                             ('May', count_range_in_list(ages, 40, 49)),
                             ('June', count_range_in_list(ages, 50, 59)),
                             ('July', count_range_in_list(ages, 60, 69)),
                             ('August', count_range_in_list(ages, 70, 79)),
                             ('September', count_range_in_list(ages, 80, 89)),
                             ('October', count_range_in_list(ages, 90, 99)),
                             ('November', count_range_in_list(ages, 100, 109)),
                             ('December', count_range_in_list(ages, 110, 120)),
                             ]'''

    return jsonify(grouped_registrations)

@statistics_blueprint.route('/monthly_reg_filter', methods=['POST'])
def monthly_reg_filter():
    month = request.get_json()['month'] if request.get_json()['month'] != '' else None
    # if no year is given, fetch results for the current year
    year = request.get_json()['year'] if request.get_json()['year'] != '' else "2021"
    facility = request.get_json()['facility'] if request.get_json()['facility'] != '' else None
    county = request.get_json()['county'] if request.get_json()['county'] != '' else None

    filtered_registrations = filter_registrations(month, year, facility, county)
    print(filtered_registrations)
    return jsonify(filtered_registrations)