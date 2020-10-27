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



def filter_data(datos, form):
    filtered_data = datos

    if (len(form.material.data) > 0 and ('MATERIAL' in datos.columns)):
        filtered_data = filtered_data[filtered_data['MATERIAL'].isin(form.material.data)]
    if (len(form.color.data) > 0  and ('COLOR' in datos.columns)):
        filtered_data = filtered_data[filtered_data['COLOR'].isin(form.color.data)]
    if (len(form.acabado.data) > 0  and ('ACABADO' in datos.columns)):
        filtered_data = filtered_data[filtered_data['ACABADO'].isin(form.acabado.data)]
    if (len(form.grosor.data) > 0  and ('GROSOR' in datos.columns)):
        filtered_data = filtered_data[filtered_data['GROSOR'].isin(form.grosor.data)]
    return (filtered_data)




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
