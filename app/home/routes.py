# -*- encoding: utf-8 -*-
"""
License: Commercial
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint

from app.base.forms import SelectionProductForm, MetrosProductForm
from flask import render_template, redirect, url_for, flash, jsonify, request
from flask_login import login_required, current_user
from app import login_manager
import flask_wtf
import wtforms
from jinja2 import TemplateNotFound
import numpy
import pandas
from functions.functions import *

df, suplementos, fregaderos, sobrante, revestimiento = read_data()


@blueprint.route('/filtro', methods = ["GET", "POST"])
@login_required
def filtro():
    material = request.args.get('jsdata')
    tabla = df
    if material:
        tabla = df.loc[df["MATERIAL"] in material]

    return render_template('banyos.html', table=tabla)





@blueprint.route('/encimeras', methods = ["POST", "GET"])
@login_required
def index():


    SelectForm = SelectionProductForm()
    MetrosForm = MetrosProductForm()

    SelectForm.material.choices = [(item,item) for item in df["MATERIAL"].unique().tolist()]
    SelectForm.material1.choices = [(item,item) for item in df["MATERIAL"].unique().tolist()]
    SelectForm.color.choices    = [(item,item) for item in df["COLOR"].unique().tolist()]
    SelectForm.acabado.choices  = [(item,item) for item in df["ACABADO"].unique().tolist()]
    SelectForm.grosor.choices   = [(item,item) for item in df["GROSOR"].unique().tolist()]


    #if not current_user.is_authenticated:
    #    return redirect(url_for('base_blueprint.login'))
    tabla=df
    if SelectForm.validate_on_submit():
        tabla = filter_data(df, SelectForm)
        SelectForm = actualizar_items(SelectForm, tabla)
        tabla = tabla[:5]

    if MetrosForm.validate_on_submit():
        tabla = calcular_precio(tabla,
                                MetrosForm.lineales.data,
                                MetrosForm.cuadrados.data,
                                MetrosForm.frentes.data)

        tabla=tabla[:1]

    return render_template(template_name_or_list = 'tbl_foo.html',
                           view_html_table       = view_html_table,
                           table                 = tabla,
                           SelectForm            = SelectForm,
                           MetrosForm            = MetrosForm,
                           segment               = 'index')










@blueprint.route('/<template>')
def route_template(template):

    #if not current_user.is_authenticated:
    #    return redirect(url_for('base_blueprint.login'))

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



