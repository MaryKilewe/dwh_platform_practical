DROP TABLE IF EXISTS patient_registration;

CREATE TABLE patient_registration (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gender TEXT NOT NULL,
    age INTEGER NOT NULL,
    facility TEXT NOT NULL,
    county TEXT NOT NULL,
    reg_date DATE NOT NULL,
    reg_month TEXT NOT NULL,
    reg_year TEXT NOT NULL
);

DROP TABLE IF EXISTS counties;
CREATE TABLE counties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);