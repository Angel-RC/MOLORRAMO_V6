# -*- encoding: utf-8 -*-
"""
License: Commercial
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SelectMultipleField
from wtforms.validators import InputRequired, Email, DataRequired

## login and registration



class LoginForm(FlaskForm):
    username = StringField    ('Username', id='username_login'   , validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login'        , validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
    username = StringField('Username'     , id='username_create' , validators=[DataRequired()])
    email    = StringField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
    password = PasswordField('Password' , id='pwd_create'      , validators=[DataRequired()])


class SelectionProductForm(FlaskForm):
    material = SelectMultipleField('material', choices=[])
    color    = SelectMultipleField('color', choices=[])
    acabado  = SelectMultipleField('acabado', choices=[])
    grosor   = SelectMultipleField('grosor', choices=[])
