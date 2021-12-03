
from flask import render_template, url_for, jsonify, flash, request, redirect
import sqlite3
#from .charts_stats import count_range_in_list

def get_db_connection():
    conn = sqlite3.connect('patient_reg.db')
    conn.row_factory = sqlite3.Row
    return conn

def filter_genders(month, year, facility, county):
    # this route returns the genders of patients registered
    if month == None:
        search_month = ""
    else:
        search_month = "reg_month = \"" + month  + "\" AND"

    if facility == None:
        search_facility = ""
    else:
        search_facility = "facility = \"" + facility  + "\" AND"

    if county == None:
        search_county = ""
    else:
        search_county = "county = \"" + county + "\" AND"


    conn = get_db_connection()
    statement = "SELECT gender, COUNT(*) FROM patient_registration WHERE {} {} {} reg_year = {} GROUP BY gender".format(search_county, search_facility, search_month, str(year))
    print(statement)
    gender_stats = conn.execute(statement).fetchall()
    conn.close()

    # format query results for the chart
    genders_stats = []
    for gender_data in gender_stats:
        genders_stats.append((gender_data[0], gender_data[1]))
    print(genders_stats)
    return genders_stats


def filter_ages(month, year, facility, county):
    # this route returns the genders of patients registered
    if month == None:
        search_month = ""
    else:
        search_month = "reg_month = \"" + month + "\" AND"

    if facility == None:
        search_facility = ""
    else:
        search_facility = "facility = \"" + facility + "\" AND"

    if county == None:
        search_county = ""
    else:
        search_county = "county = \"" + county + "\" AND"

    conn = get_db_connection()
    statement = "SELECT id, age FROM patient_registration WHERE {} {} {} reg_year = {}".format(
        search_county, search_facility, search_month, str(year))
    filtered_age_stats = conn.execute(statement).fetchall()
    conn.close()

    # format query results for the chart
    ages = []
    for gender_data in filtered_age_stats:
        ages.append(gender_data[1])

    filtered_grouped_ages = [('0 - 9', count_range_in_list(ages, 0, 9)),
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

    return filtered_grouped_ages

def count_range_in_list(li, min, max):
    ctr = 0
    for x in li:
        if min <= x <= max:
            ctr += 1
    return ctr


def filter_registrations(month, year, facility, county):
    # this route returns the filtered of monthly registrations
    if month == None:
        search_month = ""
    else:
        search_month = "reg_month = \"" + month + "\" AND"

    if facility == None:
        search_facility = ""
    else:
        search_facility = "facility = \"" + facility + "\" AND"

    if county == None:
        search_county = ""
    else:
        search_county = "county = \"" + county + "\" AND"

    conn = get_db_connection()
    statement = "SELECT reg_month, COUNT(*) FROM patient_registration WHERE {} {} {} reg_year = {} GROUP BY reg_month".format(
        search_county, search_facility, search_month, str(year))
    filtered_reg_stats = conn.execute(statement).fetchall()
    conn.close()

    # format query results for the chart
    monthly_reg = {}
    for reg_data in filtered_reg_stats:
        monthly_reg[reg_data[0]] = reg_data[1]

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

    filtered_registrations = []
    for month in months:
        if month in monthly_reg:
            filtered_registrations.append((month, monthly_reg[month]))
        else:
            filtered_registrations.append((month, 0))

    return filtered_registrations