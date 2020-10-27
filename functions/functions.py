import numpy as np
import pandas as pd


def view_html_table(table, clase="display table table-hover", id = "myTable"):
    html = table.to_html(classes     = clase,
                         table_id    = id,
                         float_format='{:8.2f}€'.format,
                         header      = True,
                         na_rep      = "",
                         index_names = False,
                         index       = False,
                         border      = 0,
                         justify     = "center")
    return (html)



def filter_data(datos, SelectForm):
    filtered_data = datos

    if (len(SelectForm.material.data) > 0 ):
        filtered_data = filtered_data[filtered_data['MATERIAL'].isin(SelectForm.material.data)]
    if (len(SelectForm.color.data) > 0  and ('COLOR' in datos.columns)):
        filtered_data = filtered_data[filtered_data['COLOR'].isin(SelectForm.color.data)]
    if (len(SelectForm.acabado.data) > 0  and ('ACABADO' in datos.columns)):
        filtered_data = filtered_data[filtered_data['ACABADO'].isin(SelectForm.acabado.data)]
    if (len(SelectForm.grosor.data) > 0  and ('GROSOR' in datos.columns)):
        filtered_data = filtered_data[filtered_data['GROSOR'].isin(SelectForm.grosor.data)]

    return (filtered_data)

def actualizar_items(form, tabla):

    form.color.choices    = [(item,item) for item in tabla["COLOR"].unique().tolist()]
    form.acabado.choices  = [(item,item) for item in tabla["ACABADO"].unique().tolist()]
    form.grosor.choices   = [(item,item) for item in tabla["GROSOR"].unique().tolist()]
    return(form)


def read_data():

    datos = pd.read_excel(io         = "data/Molorramo_productos.xlsx",
                          sheet_name = "productos_molorramo")\
        .fillna(" ")\
        .assign(hack='')\
        .set_index('hack')

    suplementos = pd.read_excel(io="data/Molorramo_productos.xlsx",
                                sheet_name="suplementos") \
        .fillna(" ") \
        .assign(hack='') \
        .set_index('hack')

    revestimiento = pd.read_excel(io="data/Molorramo_productos.xlsx",
                                sheet_name="revestimiento") \
        .fillna(" ") \
        .assign(hack='') \
        .set_index('hack')

    fregaderos = pd.read_excel(io         = "data/Molorramo_productos.xlsx",
                               sheet_name = "fregaderos")\
        .fillna(" ")\
        .assign(hack='')\
        .set_index('hack')

    sobrante = pd.read_excel(io         = "data/Molorramo_productos.xlsx",
                             sheet_name = "piezas_sobrantes")


    sobrante["LARGO"] = sobrante["LARGO"] / 100

    sobrante["ANCHO"] = sobrante["ANCHO"] / 100
    sobrante  = sobrante[sobrante["FECHA_SALIDA"].isnull()].fillna(" ")
    sobrante["VENDIDO"] = False
    sobrante["MEDIDA_PIEZA"] = sobrante['LARGO'].map(str) + ' X ' + sobrante['ANCHO'].map(str)
    sobrante = pd.merge(sobrante, datos, how='left',
                        on=["MATERIAL", "COLOR", "GROSOR", "ACABADO"]).assign(hack='').set_index('hack')
    sobrante["PRECIO_ML"] =sobrante["PRECIO_ML"] * 0.75
    sobrante["PRECIO_M2"] =sobrante["PRECIO_M2"] * 0.75
    sobrante.loc[sobrante["PRECIO_ML"].isnull(), 'PRECIO_ML'] = 150
    sobrante.loc[sobrante["PRECIO_M2"].isnull(), 'PRECIO_M2'] = 250

    return (datos, suplementos, fregaderos, sobrante, revestimiento)



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


