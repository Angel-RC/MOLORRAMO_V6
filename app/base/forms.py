# -*- encoding: utf-8 -*-
"""
License: Commercial
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SelectMultipleField,SubmitField, BooleanField, FloatField
from wtforms.validators import InputRequired, Email, DataRequired, NumberRange

## login and registration
class LoginForm(FlaskForm):
    email        = StringField('Email',          id='email_login',   validators = [DataRequired()])
    password     = PasswordField('Password',     id='pwd_login',     validators = [DataRequired()])
    password_old = PasswordField('Password_old', id='pwd_old_login', validators = [DataRequired()])

class CreateAccountForm(FlaskForm):
    email    = StringField('Email',       id='email_create', validators=[DataRequired(), Email()])
    password = PasswordField('Password' , id='pwd_create',   validators=[DataRequired()])

class SelectionEncimerasForm(FlaskForm):
    material  = SelectMultipleField('material', choices = [])
    color     = SelectMultipleField('color',    choices = [])
    acabado   = SelectMultipleField('acabado',  choices = [])
    grosor    = SelectMultipleField('grosor',   choices = [])
    promocion = BooleanField("promocion", default = "checked")
    lineales  = FloatField("lineales",    default = 0.0,validators=[NumberRange(min=0, max=100)])
    cuadrados = FloatField("cuadrados",   default = 0.0,validators=[NumberRange(min=0, max=100)])
    frentes   = FloatField("frentes",     default = 0.0,validators=[NumberRange(min=0, max=100)])


class SelectionInventarioForm(FlaskForm):
    material  = SelectMultipleField('material', choices=[])
    color     = SelectMultipleField('color', choices=[])
    acabado   = SelectMultipleField('acabado', choices=[])
    grosor    = SelectMultipleField('grosor', choices=[])
    medida    = SelectMultipleField('medida', choices=[])


class SelectionSuplementosForm(FlaskForm):
    concepto = SelectMultipleField('concepto', choices=[])
    cantidad = FloatField("cantidad", default = 0.0, validators=[NumberRange(min=0, max=10000)])
    carrito = SubmitField('carrito')


class FacturasForm(FlaskForm):
    pvp = FloatField("pvp", default = 0.0)
    confirmar = SubmitField('confirmar')
