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
from app.base.models import Pedido
from datetime import date


@blueprint.route('/filter_data', methods = ["POST", "GET"])
def filter_data():
    body = request.get_json(force= True)
    data = pd.DataFrame(body["data"])
    data_filter = data
    for key, value in body["Filtros"].items():

        if len(value) > 0 and (key.upper() in data_filter.columns):
            filtro = pd.DataFrame.from_records(value)
            filtro = filtro["value"].to_list()

            data_filter = data_filter[data_filter[key.upper()].isin(filtro)]


    if (body["page"] == "suplementos"):
        data_filter["CANTIDAD"] = body["Filtros"]["cantidad"][0] + " " + data_filter["TIPO_COSTE"]
        data_filter["TOTAL"] = int(body["Filtros"]["cantidad"][0]) * data_filter["PRECIO_UNIDAD"]

    options = {}
    options["material"] = get_options(data, "MATERIAL")
    options["concepto"] = get_options(data, "CONCEPTO")
    options["color"] = get_options(data_filter, "COLOR")
    options["acabado"] = get_options(data_filter, "ACABADO")
    options["medida"] = get_options(data_filter, "MEDIDA")
    options["grosor"] = get_options(data_filter, "GROSOR")
    options["grupo"] = get_options(data_filter, "grupo")
    options["idpedido"] = get_options(data_filter, "id_pedido")
    options["usuario"] = get_options(data_filter, "usuario")
    options["estado"] = get_options(data_filter, "estado")


    data_filter = convertPandasToJson(data_filter)

    return {"data": data_filter,
            "options": options}


@blueprint.route('/create_data_inicial', methods = ["POST", "GET"])
def create_data_inicial():
    body = request.get_json(force=True)

    data = pd.read_excel("./data/angel_pruebas.xlsx", sheet_name = body["page"])


    if (body["page"] == "inventario"):
        data = calcular_precio_inventario(data)
    if (body["page"] == "encimeras"):

        if float(body["Metros"]["lineales"]) + float(body["Metros"]["cuadrados"]) + float(body["Metros"]["frente"]) > 0:
            if body["Metros"]["promocion"]:
                data = data[data["MAXIMO_SOBRANTE"] == 0]
            if float(body["Metros"]["lineales"])>0 and (float(body["Metros"]["cuadrados"]) + float(body["Metros"]["frente"])) == 0:
                body["Metros"]["lineales"] = max(3, float(body["Metros"]["lineales"]))

            data = calcular_precio(data,
                                   float(body["Metros"]["lineales"]),
                                   float(body["Metros"]["cuadrados"]),
                                   float(body["Metros"]["frente"]))

            data = mis_encimeras(data,
                                 float(body["Metros"]["lineales"]),
                                 float(body["Metros"]["cuadrados"]),
                                 float(body["Metros"]["frente"]))

        else:
            data = []

    options = {}
    options["material"] = get_options(data, "MATERIAL")
    options["color"] = get_options(data, "COLOR")
    options["acabado"] = get_options(data, "ACABADO")
    options["concepto"] = get_options(data, "CONCEPTO")
    options["medida"] = get_options(data, "MEDIDA")
    options["grosor"] = get_options(data, "GROSOR")



    data = data.rename(columns={'PRECIO': 'TOTAL'})
    data = convertPandasToJson(data)


    return {"data": data,
            "options": options}








@blueprint.route('/mis_pedidos', methods = ["POST", "GET"])
def mis_pedidos():
    data = pd.read_sql('pedidos', db.engine)
    usuarios = pd.read_sql('usuarios', db.engine)

    data = pd.merge(data, usuarios, left_on='id_cliente', right_on='id', how="inner")

    options = {}
    options["grupo"] = get_options(data, "grupo")
    options["idpedido"] = get_options(data, "id_pedido")
    options["usuario"] = get_options(data, "username")
    options["estado"] = get_options(data, "estado")


    data = convertPandasToJson(data)

    return {"data": data,
            "options": options}


