# -*- encoding: utf-8 -*-
"""
License: Commercial
Copyright (c) 2019 - present AppSeed.us
"""

from app import db
from app.home import blueprint
from app.base.models import *
from app.base.forms import SelectionEncimerasForm, FacturasForm, SelectionInventarioForm, SelectionSuplementosForm
from flask import render_template, redirect, url_for, flash, jsonify, request, session
from flask_login import login_required, current_user
from app import login_manager
import flask_wtf
import wtforms
from jinja2 import TemplateNotFound
import numpy as np
import pandas as pd
from functions.functions import *
from datetime import date


@blueprint.route('/factura', methods = ["POST", "GET"])
@login_required
def factura():
    return({})





@blueprint.route('/encimeras', methods = ["POST", "GET"])
def index():
    return app.send_static_file("index.html")


@blueprint.route('/inventario', methods=["POST", "GET"])
@login_required
def page_inventario():
    return({})


@blueprint.route('/suplementos', methods=["POST", "GET"])
@login_required
def page_suplementos():
    return({})


@blueprint.route('/panel', methods=["POST", "GET"])
@login_required
def panel():
    return({})



@blueprint.route('/presupuestos', methods=["POST", "GET"])
@login_required
def page_presupuestos():
   
   return({})
#
# @blueprint.route('/encimeras2', methods=["POST", "GET"])
# @login_required
# def index2():
#     users_schema = UserSchema(many=True)
#     tabla = User.query.all()
#
#     return render_template(template_name_or_list='01_prueba.html',
#                            data=tabla,
#                            segment='index')
#
#
# @blueprint.route('/livesearch', methods=["POST", "GET"])
# @login_required
# def index3():
#     from os import environ
#     from sqlalchemy import create_engine, MetaData, Table
#     from sqlalchemy.orm import scoped_session, sessionmaker
#     SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
#         environ.get('APPSEED_DATABASE_USER', 'wexblshovbqplg'),
#         environ.get('APPSEED_DATABASE_PASSWORD', 'd2f882c81122eecf11e18c38d45dd07fc0edb3e577f2870429f75a8f9446d1c2'),
#         environ.get('APPSEED_DATABASE_HOST', 'ec2-54-217-206-236.eu-west-1.compute.amazonaws.com'),
#         environ.get('APPSEED_DATABASE_PORT', 5432),
#         environ.get('APPSEED_DATABASE_NAME', 'd561hb6caco114'))
#     engine = create_engine(SQLALCHEMY_DATABASE_URI)
#
#     da = pd.read_sql('encimeras', engine)
#
#     return (da.to_json(orient="records"))
#
#
# @blueprint.route('/prueba', methods=["POST", "GET"])
# @login_required
# def page_pruebas():
#     if not current_user.is_authenticated:
#         return redirect(url_for('base_blueprint.login'))
#
#     ma = Marshmallow()
#     SuplementForm = SelectionProductForm()
#
#     tabla = Encimeras.query.filter_by(MATERIAL="DEKTON").all()
#
#     from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
#
#     class UserSchema(ma.ModelSchema):
#         class Meta:
#             model = User
#
#     users_schema = UserSchema()
#     all_users = User.query.first()
#     out = users_schema.dump(all_users).data
#     data = jsonify({"user": out})
#
#     return render_template(template_name_or_list='00_prueba.html',
#                            view_html_table=view_html_table,
#                            users=tabla,
#                            data=data,
#                            SelectForm=SuplementForm,
#                            segment='prueba')
#
#
# @blueprint.route('/<template>')
# def route_template(template):
#     if not current_user.is_authenticated:
#         return redirect(url_for('base_blueprint.login'))
#
#     try:
#
#         # Flexible rendering
#         # Sample pattern: '/profile' AND '/profile.html'
#         if not template.endswith('.html'):
#             template += '.html'
#
#         return render_template(template)
#
#     except TemplateNotFound:
#         return render_template('page-404.html'), 404
#
#     except:
#         return render_template('page-500.html'), 500

