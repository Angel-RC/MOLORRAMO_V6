# -*- encoding: utf-8 -*-
"""
License: Commercial
Copyright (c) 2019 - present AppSeed.us
"""
from threading import Thread
import flask_mail
import pandas as pd
from app.base.util import hash_pass
from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

from app import db, login_manager
from app.base import blueprint
from app.base.forms import LoginForm, CreateAccountForm
from app.base.models import User
from functions.functions import *
from app.base.util import verify_pass

@blueprint.route('/')
def route_default():
    return({})

@blueprint.route('/error-<error>')
def route_errors(error):
    return({})

## Login & Registration

@blueprint.route('/login', methods=['GET', 'POST'])
def login():

    body = request.get_json(force=True)

    email = body['email']
    password = body['password']

    # Locate user
    print(email)
    user = User.query.filter_by(email=email).first()
    print(user)
    if user and password == "qqqq":

        return {"email": user.email,
                "level": user.level,
                "username": user.username}

    return {"msg": "Error",
            "status": 0}


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    body = request.get_json(force=True)

    email = body['email']
    password = body["password"]

    user = User.query.filter_by(email=email).first()
    if user:
        return {"msg": 'Email ya registrado'}

        # else we can create the user
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return ({'Bien. Email registrado'})


@blueprint.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    form = LoginForm(request.form)
    if 'reset' in request.form:

        email        = request.form['email']
        password     = request.form['password']
        password_old = request.form['password_old']

        user = User.query.filter_by(email=email).first()

        if user and verify_pass(password_old, user.password):
            user.password = hash_pass(password)
            db.session.commit()
            return render_template('accounts/reset_password.html', msg='Contraseña cambiada', form=form)

        return render_template('accounts/reset_password.html', msg='Email o contraseña incorrectos', form=form)

    else:
        return render_template('accounts/reset_password.html', form=form)





@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('base_blueprint.login'))

@blueprint.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

## Errors

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('errors/403.html'), 403

@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('errors/403.html'), 403

@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


import uuid

def make_key():
    return uuid.uuid4()