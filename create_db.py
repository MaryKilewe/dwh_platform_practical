import sqlite3

connection = sqlite3.connect('patient_reg.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO patient_registration (first_name, last_name, gender, age, facility, county, reg_date,reg_month,reg_year) VALUES (?, ?, ?, ?, ?, ?, ?,?,?)",
            ('Melissa', 'Kamau', 'Female', 32, 'Nairobi Hospital', 'Nairobi', '2020-08-27', 'August', '2020')
            )

cur.execute("INSERT INTO patient_registration (first_name, last_name, gender, age, facility, county, reg_date,reg_month,reg_year) VALUES (?, ?, ?, ?, ?, ?, ?,?,?)",
            ('Robert', 'Kimathi', 'Male', 40, 'Matta Hospital', 'Mombasa', '2021-08-24', 'August', '2021')
            )

counties_list = ["Mombasa","Kwale","Kilifi","Tana River","Lamu","Taita/Taveta","Garissa","Wajir","Mandera","Marsabit",
                 "Isiolo","Meru","Tharaka-Nithi","Embu","Kitui","Machakos","Makueni","Nyandarua","Nyeri",
                 "Kirinyaga","Murang'a","Kiambu","Turkana","West Pokot","Samburu","Trans Nzoia","Uasin Gishu",
                 "Elgeyo/Marakwet","Nandi","Baringo","Laikipia","Nakuru","Narok","Kajiado","Kericho","Bomet","Kakamega",
                 "Vihiga","Bungoma","Busia","Siaya","Kisumu","Homa Bay","Migori","Kisii","Nyamira","Nairobi"
                ]

for county in counties_list:
    cur.execute("INSERT INTO counties (name) VALUES (?)",
                (county,)
                )

connection.commit()
connection.close()