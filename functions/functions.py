from geopy.geocoders import Nominatim, GoogleV3
import pandas as pd
import json
import numpy as np
from io import BytesIO

def convertBytesToJson(bytes):
    df = pd.read_csv(BytesIO(bytes), sep = ";")
    parsed = convertPandasToJson(df)
    return parsed

def convertPandasToJson(data):
    result = data.to_json(orient="records")
    parsed = json.loads(result)
    return parsed

def get_options(data, variable):
    options = []
    if variable in data.columns:
        options = pd.DataFrame(data[variable].unique(), columns=["label"])
        options["value"] = options["label"]

        options = convertPandasToJson(options)

    return options



def calcular_precio(datos, metros_lineales, metros_cuadrados, metros_frente):
    tipos_metros = (metros_lineales > 0.0) + (metros_cuadrados > 0.0) + (metros_frente > 0.0)

    sobra = 0.0

    if (metros_lineales > 0 and (metros_lineales % 6.3) != 0.0):
        sobra = (6.3 - metros_lineales % 6.3) * 0.7
        if sobra > 2.15:
            sobra = datos["MEDIDA_TABLA"] - 0.7 * (metros_lineales % 6.3)
    datos["SOBRANTE"] = sobra
    if ((metros_cuadrados + metros_frente) > 0.0):
        datos["SOBRANTE"] = sobra - (metros_cuadrados + metros_frente)

        datos.loc[datos["SOBRANTE"] < 0.0, "SOBRANTE"] = (datos.loc[datos["SOBRANTE"] < 0.0, "MEDIDA_TABLA"] - (
                    (metros_cuadrados + metros_frente - sobra) % datos.loc[datos["SOBRANTE"] < 0.0, "MEDIDA_TABLA"]))

    datos["SOBRANTE"] = np.minimum(datos["SOBRANTE"], datos["MAXIMO_SOBRANTE"])

    datos.loc[datos["SOBRANTE"] > datos["MEDIDA_TABLA"] - 0.001, "SOBRANTE"] = 0.0
    if metros_lineales > 0.0:
        datos["PRECIO_ML"] = (datos["PRECIO_ML"] + (
                    datos["SOBRANTE"] * datos["COSTE_M2"] / tipos_metros) / metros_lineales).apply(np.ceil)
    if metros_cuadrados > 0.0:
        datos["PRECIO_M2"] = (datos["PRECIO_M2"] + (
                    datos["SOBRANTE"] * datos["COSTE_M2"] / tipos_metros) / metros_cuadrados).apply(np.ceil)
    if metros_frente > 0.0:
        datos["PRECIO_FRENTES_M2"] = (datos["PRECIO_FRENTES_M2"] + (
                    datos["SOBRANTE"] * datos["COSTE_FRENTES_M2"] / tipos_metros) / metros_frente).apply(np.ceil)
    return (datos)





def mis_encimeras(mis_productos,metros_lineales, metros_cuadrados, metros_frente):
    mis_productos_style = pd.DataFrame()
    if (metros_lineales + metros_cuadrados + metros_frente > 0):

        if metros_lineales > 0:
            mis_productos["MEDIDA"] = str(metros_lineales) + " M. lineales"
            mis_productos["PRECIO_METRO"] = mis_productos["PRECIO_ML"]
            mis_productos["TOTAL"] = mis_productos["PRECIO_METRO"] * metros_lineales

            mis_productos_style = pd.concat([mis_productos_style, mis_productos])
        if metros_cuadrados > 0:
            mis_productos["MEDIDA"] = str(metros_cuadrados) + " M. cuadrados"
            mis_productos["PRECIO_METRO"] = mis_productos["PRECIO_M2"]
            mis_productos["TOTAL"] = mis_productos["PRECIO_METRO"] * metros_cuadrados
            mis_productos_style = pd.concat([mis_productos_style, mis_productos])

        if metros_frente > 0:
            mis_productos["MEDIDA"] = str(metros_frente) + " M. frente"
            mis_productos["PRECIO_METRO"] = mis_productos["PRECIO_FRENTES_M2"]
            mis_productos["TOTAL"] = mis_productos["PRECIO_METRO"] * metros_frente
            mis_productos_style = pd.concat([mis_productos_style, mis_productos])

        mis_productos_style["TOTAL"] = (mis_productos_style["TOTAL"]).apply(np.round)
        mis_productos_style = mis_productos_style[mis_productos_style["TOTAL"] > 0.0]
        mis_productos_style = mis_productos_style[
            ["MATERIAL", "COLOR", "ACABADO", "GROSOR", "MEDIDA", "PRECIO_METRO",
             "TOTAL"]]

    return(mis_productos_style)



def calcular_precio_inventario(data):

    data = data[data.MATERIAL.notnull()]




    datos = pd.read_excel("./data/angel_pruebas.xlsx", sheet_name = "encimeras") \
        .fillna(" ") \
        .assign(hack='') \
        .set_index('hack')


    data["LARGO"] = data["LARGO"] / 100

    data["ANCHO"] = data["ANCHO"] / 100
    data = data[data["FECHA_SALIDA"].isnull()].fillna(" ")
    data["VENDIDO"] = False
    data["MEDIDA_PIEZA"] = data['LARGO'].map(str) + ' X ' + data['ANCHO'].map(str)
    data = pd.merge(data, datos, how='left',
                    on=["MATERIAL", "COLOR", "GROSOR", "ACABADO"]).assign(hack='').set_index('hack')

    data["PRECIO_M2"] = data["PRECIO_M2"] * 0.75
    data.loc[data["PRECIO_M2"].isnull(), 'PRECIO_M2'] = 250

    data["PRECIO_METRO"] = data["PRECIO_M2"]
    data["PRECIO_TABLA"] = data["PRECIO_METRO"] * data["LARGO"] * data["ANCHO"]
    data = data[["MATERIAL", "COLOR", "ACABADO", "GROSOR", "MEDIDA_PIEZA", "PRECIO_M2",
                 "PRECIO_TABLA", "FECHA_ENTRADA", "FECHA_SALIDA", "ID"]]

    data = data.rename(columns={'MEDIDA_PIEZA': 'MEDIDA', "PRECIO_TABLA": "TOTAL"})

    return data
