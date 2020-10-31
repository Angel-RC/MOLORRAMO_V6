# -*- encoding: utf-8 -*-
"""
License: Commercial
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SelectMultipleField, BooleanField, FloatField
from wtforms.validators import InputRequired, Email, DataRequired, NumberRange

## login and registration



class LoginForm(FlaskForm):
    username = StringField    ('Username', id='username_login'   , validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login'        , validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
    username = StringField('Username'     , id='username_create' , validators=[DataRequired()])
    email    = StringField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
    password = PasswordField('Password' , id='pwd_create'      , validators=[DataRequired()])


class SelectionProductForm(FlaskForm):
    material  = SelectMultipleField('material', choices=[])
    concepto  = SelectMultipleField('concepto', choices=[])
    color     = SelectMultipleField('color', choices=[])
    acabado   = SelectMultipleField('acabado', choices=[])
    grosor    = SelectMultipleField('grosor', choices=[])
    promocion = BooleanField("promocion", default="checked")
    lineales  = FloatField("lineales",default=0.0,validators=[NumberRange(min=0, max=100)])
    cuadrados = FloatField("cuadrados",default=0.0,validators=[NumberRange(min=0, max=100)])
    frentes   = FloatField("frentes",default=0.0,validators=[NumberRange(min=0, max=100)])
    cantidad  = FloatField("cantidad",default=0.0,validators=[NumberRange(min=0, max=100)])
