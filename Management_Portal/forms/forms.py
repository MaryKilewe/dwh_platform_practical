from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,\
    IntegerField, SelectField, TextAreaField, RadioField, MultipleFileField, HiddenField,DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, ValidationError,\
    Optional, InputRequired, Regexp


class PatientRegForm(FlaskForm):
    ''' Facilitates addition of newly registered patients '''

    first_name = StringField('First Name', validators=[DataRequired(), Regexp('^\w+$', message="Username must contain only letters numbers or underscore"), Length(min=2, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=30)])
    gender = SelectField('Gender', choices=[ ('Female', 'Female'), ('Male', 'Male')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=150)])
    facility = StringField('Health Facility', validators=[DataRequired(), Length(min=2, max=60)])
    county = SelectField('County', choices=[])
    reg_date = DateField('Registration Date', validators=[DataRequired()])

    submit = SubmitField('Add')


class FilterForm(FlaskForm):
    ''' Facilitates addition of newly registered patients '''
    facility = SelectField('Health Facilities')
    county = SelectField('County', choices=[])
    month = SelectField('Month')
    year = SelectField('Year', default=2021)

    submit = SubmitField('Filter')
