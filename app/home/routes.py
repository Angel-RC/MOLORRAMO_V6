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

today = date.today().strftime("%d/%m/%Y")

class empresa:
    def __init__(self, name, address, tlfno, mail):
        self.name = name
        self.address = address
        self.tlfno = tlfno
        self.mail = mail

df, suplementos, fregaderos, sobrante, revestimiento = read_data()


@blueprint.route('/factura', methods = ["POST", "GET"])
@login_required
def factura():
    form = FacturasForm()

    molorramo = empresa(name = "Molorramo",
                        address = "Mota del Cuervo (Cuenca)",
                        tlfno = "666666666",
                        mail = "mariluz@molorramo.com")

    cliente = empresa(name = "Cliente 1",
                        address = "Burjassot (Valencia)",
                        tlfno = "999999999",
                        mail = "cristina@cliente1.com")

    encimeras   = pd.DataFrame()
    inventario  = pd.DataFrame()
    suplementos = pd.DataFrame()

    pvp = 0.0
    total = 0.0
    if form.validate_on_submit():
        pvp = form.pvp.data / 100

    if not session.get("encimeras_compradas") is None:
        encimeras = session.get("encimeras_compradas")
        encimeras = pd.read_json(encimeras)
        encimeras["TOTAL"] = encimeras["TOTAL"] * (1 + pvp)
        encimeras["PRECIO_METRO"] = encimeras["PRECIO_METRO"] * (1 + pvp)
        total = total + encimeras["TOTAL"].sum()
    if not session.get("inventario_comprado") is None:
        inventario = session.get("inventario_comprado")
        inventario = pd.read_json(inventario)
        inventario["PRECIO_M2"] = inventario["PRECIO_M2"] * (1 + pvp)
        inventario["PRECIO_TABLA"] = inventario["PRECIO_TABLA"] * (1 + pvp)
        total = total + inventario["PRECIO_TABLA"].sum()
    if not session.get("suplementos_comprados") is None:
        suplementos = session.get("suplementos_comprados")
        suplementos = pd.read_json(suplementos)
        suplementos["TOTAL"] = suplementos["TOTAL"] * (1 + pvp)
        total = total + suplementos["TOTAL"].sum()


    return render_template(template_name_or_list = '00_factura.html',
                           Molorramo       = molorramo,
                           Cliente         = cliente,
                           id_factura      = 123123,
                           view_html_table = view_html_table,
                           today           = today,
                           form            = form,
                           encimeras       = encimeras,
                           inventario      = inventario,
                           suplementos     = suplementos,
                           total           = str(total)+ " €",
                           pagado          = "0.00 €",
                           a_pagar         = str(total)+ " €",
                           segment         = 'factura')





@blueprint.route('/encimeras', methods = ["POST", "GET"])
@login_required
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))



    form = SelectionEncimerasForm()


    form.material.choices = [(item,item) for item in df["MATERIAL"].unique().tolist()]
    form.color.choices    = [(item,item) for item in df["COLOR"].unique().tolist()]
    form.acabado.choices  = [(item,item) for item in df["ACABADO"].unique().tolist()]
    form.grosor.choices   = [(item,item) for item in df["GROSOR"].unique().tolist()]

    tabla = pd.DataFrame()
    if form.validate_on_submit():

        tabla = filter_data(df, form)
        form = actualizar_items(form, tabla)
        tabla = calcular_precio(tabla,
                                form.lineales.data,
                                form.cuadrados.data,
                                form.frentes.data)
        tabla = mis_encimeras(tabla,
                                form.lineales.data,
                                form.cuadrados.data,
                                form.frentes.data)

    if "carrito" in request.form:
        encimeras = actualizar_session(session, "encimeras_compradas", tabla)


    return render_template(template_name_or_list = '00_encimeras.html',
                           view_html_table       = view_html_table,
                           table                 = tabla,
                           form                  = form,
                           segment               = 'index')


@blueprint.route('/inventario', methods=["POST", "GET"])
@login_required
def page_inventario():
    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    form = SelectionInventarioForm()

    form.material.choices = [(item, item) for item in sobrante["MATERIAL"].unique().tolist()]
    form.color.choices    = [(item, item) for item in sobrante["COLOR"].unique().tolist()]
    form.acabado.choices  = [(item, item) for item in sobrante["ACABADO"].unique().tolist()]
    form.grosor.choices   = [(item, item) for item in sobrante["GROSOR"].unique().tolist()]
    form.medida.choices   = [(item, item) for item in sobrante["MEDIDA_PIEZA"].unique().tolist()]

    tabla = sobrante
    if form.validate_on_submit():
        tabla = filter_inventario(tabla, form)
        form = actualizar_items(form, tabla)
        form.medida.choices = [(item, item) for item in tabla["MEDIDA_PIEZA"].unique().tolist()]

    if "carrito" in request.form:
        carrito = actualizar_session(session, "inventario_comprado", tabla)

    return render_template(template_name_or_list = '00_inventario.html',
                           view_html_table       = view_html_table,
                           table                 = tabla,
                           form                  = form,
                           segment               = 'inventario')


@blueprint.route('/suplementos', methods=["POST", "GET"])
@login_required
def page_suplementos():
    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    form = SelectionSuplementosForm()

    form.concepto.choices = [(item, item) for item in suplementos["CONCEPTO"].unique().tolist()]

    tabla = suplementos
    if form.validate_on_submit():
        tabla = tabla[tabla['CONCEPTO'].isin(form.concepto.data)]

        tabla["CANTIDAD"] = str(form.cantidad.data) + " " + tabla["TIPO_COSTE"]
        tabla["TOTAL"] = form.cantidad.data * tabla["PRECIO_UNIDAD"]

    if "carrito" in request.form:
        carrito = actualizar_session(session, "suplementos_comprados", tabla)

    return render_template(template_name_or_list = '00_suplementos.html',
                           view_html_table       = view_html_table,
                           table                 = tabla,
                           form                  = form,
                           segment               = 'suplementos')


@blueprint.route('/panel', methods=["POST", "GET"])
@login_required
def panel():
    return render_template(template_name_or_list = '00_panel.html',
                           segment               = 'panel')



@blueprint.route('/presupuestos', methods=["POST", "GET"])
@login_required
def page_presupuestos():
    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    form = PresupuestosForm()

    encimeras   = pd.DataFrame()
    inventario  = pd.DataFrame()
    suplementos = pd.DataFrame()

    pvp = 0.0
    if form.validate_on_submit():
        pvp = form.pvp.data / 100


    if not session.get("encimeras_compradas") is None:
        encimeras = session.get("encimeras_compradas")
        encimeras = pd.read_json(encimeras)
        encimeras["TOTAL"] = encimeras["TOTAL"] * (1 + pvp)
        encimeras["PRECIO_METRO"] = encimeras["PRECIO_METRO"] * (1 + pvp)
    if not session.get("inventario_comprado") is None:
        inventario = session.get("inventario_comprado")
        inventario = pd.read_json(inventario)
        inventario["PRECIO_M2"] = inventario["PRECIO_M2"] * (1 + pvp)
        inventario["PRECIO_TABLA"] = inventario["PRECIO_TABLA"] * (1 + pvp)
    if not session.get("suplementos_comprados") is None:
        suplementos = session.get("suplementos_comprados")
        suplementos = pd.read_json(suplementos)
        suplementos["TOTAL"] = suplementos["TOTAL"] * (1 + pvp)

    return render_template(template_name_or_list = '00_presupuestos.html',
                           view_html_table       = view_html_table,
                           encimeras             = encimeras,
                           suplementos           = suplementos,
                           inventario            = inventario,
                           form                  = form,
                           segment               = 'presupuestos')

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

