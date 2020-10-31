# -*- encoding: utf-8 -*-
"""
License: Commercial
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint

from app.base.forms import SelectionProductForm
from flask import render_template, redirect, url_for, flash, jsonify, request, session
from flask_login import login_required, current_user
from app import login_manager
import flask_wtf
import wtforms
from jinja2 import TemplateNotFound
import numpy as np
import pandas as pd
from functions.functions import *

df, suplementos, fregaderos, sobrante, revestimiento = read_data()





@blueprint.route('/encimeras', methods = ["POST", "GET"])
@login_required
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))


    SelectForm = SelectionProductForm()


    SelectForm.material.choices = [(item,item) for item in df["MATERIAL"].unique().tolist()]
    SelectForm.color.choices    = [(item,item) for item in df["COLOR"].unique().tolist()]
    SelectForm.acabado.choices  = [(item,item) for item in df["ACABADO"].unique().tolist()]
    SelectForm.grosor.choices   = [(item,item) for item in df["GROSOR"].unique().tolist()]

    tabla = pd.DataFrame()
    if SelectForm.validate_on_submit():

        tabla = filter_data(df, SelectForm)
        SelectForm = actualizar_items(SelectForm, tabla)
        tabla = calcular_precio(tabla,
                                SelectForm.lineales.data,
                                SelectForm.cuadrados.data,
                                SelectForm.frentes.data)
        tabla = mis_encimeras(tabla,
                                SelectForm.lineales.data,
                                SelectForm.cuadrados.data,
                                SelectForm.frentes.data)

    if "carrito" in request.form:
        session["encimeras_compradas"] = tabla.to_json(orient='records')


    return render_template(template_name_or_list = '00_encimeras.html',
                           view_html_table       = view_html_table,
                           table                 = tabla,
                           SelectForm            = SelectForm,
                           segment               = 'index')



@blueprint.route('/banyos', methods = ["POST", "GET"])
@login_required
def page_banyos():
    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))


    SelectForm = SelectionProductForm()


    SelectForm.material.choices = [(item,item) for item in sobrante["MATERIAL"].unique().tolist()]
    SelectForm.color.choices    = [(item,item) for item in sobrante["COLOR"].unique().tolist()]
    SelectForm.acabado.choices  = [(item,item) for item in sobrante["ACABADO"].unique().tolist()]
    SelectForm.grosor.choices   = [(item,item) for item in sobrante["GROSOR"].unique().tolist()]


    tabla = sobrante
    if SelectForm.validate_on_submit():
        tabla = filter_data(tabla, SelectForm)
        SelectForm = actualizar_items(SelectForm, tabla)


    if "carrito" in request.form:
        session["banyos_comprados"] = tabla.to_json(orient='records')

    return render_template(template_name_or_list = '01_banyos.html',
                           view_html_table       = view_html_table,
                           table                 = tabla,
                           SelectForm            = SelectForm,
                           segment               = 'banyos')



@blueprint.route('/suplementos', methods = ["POST", "GET"])
@login_required
def page_suplementos():
    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))


    SuplementForm = SelectionProductForm()


    SuplementForm.concepto.choices = [(item,item) for item in suplementos["CONCEPTO"].unique().tolist()]


    tabla=suplementos
    if SuplementForm.validate_on_submit():

        tabla = tabla[tabla['CONCEPTO'].isin(SuplementForm.concepto.data)]

        tabla["CANTIDAD"] = str(SuplementForm.cantidad.data) + " " + tabla["TIPO_COSTE"]
        tabla["PRECIO_TOTAL"] = SuplementForm.cantidad.data * tabla["PRECIO_UNIDAD"]


    if "carrito" in request.form:
        session["suplementos_comprados"] = tabla.to_json(orient='records')

    return render_template(template_name_or_list = '02_suplementos.html',
                           view_html_table       = view_html_table,
                           table                 = tabla,
                           SelectForm            = SuplementForm,
                           segment               = 'suplementos')


@blueprint.route('/presupuestos', methods = ["POST", "GET"])
@login_required
def page_presupuestos():
    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    SelectForm = SelectionProductForm()

    encimeras = pd.DataFrame()
    banyos = pd.DataFrame()
    suplementos = pd.DataFrame()

    if not session.get("encimeras_compradas") is None:
        encimeras = session.get("encimeras_compradas")
        encimeras = pd.read_json(encimeras)
    if not session.get("banyos_comprados") is None:
        banyos = session.get("banyos_comprados")
        banyos = pd.read_json(banyos)
    if not session.get("suplementos_comprados") is None:
        suplementos = session.get("suplementos_comprados")
        suplementos = pd.read_json(suplementos)


    return render_template(template_name_or_list = '00_presupuestos.html',
                           view_html_table       = view_html_table,
                           encimeras             = encimeras,
                           suplementos = suplementos,
                           banyos=banyos,
                           SelectForm            = SelectForm,
                           segment               = 'suplementos')




@blueprint.route('/<template>')
def route_template(template):

    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    try:

        # Flexible rendering 
        # Sample pattern: '/profile' AND '/profile.html' 
        if not template.endswith( '.html' ):
            template += '.html'

        return render_template(template)

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500



