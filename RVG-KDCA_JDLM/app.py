import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import math
import time

#import fronted
from fronted.main import layout
from backend.fases_del_suelo import *
from fronted.grupo2.titulo2 import *


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout


#Datos relación volumétrica
@app.callback(
    Output('fases_del_suelo_vol', 'children'),
    Input('volumen_solidos', 'value'),
    Input('volumen_agua', 'value'),
    Input('volumen_aire', 'value'),
)

def volumen_total(volumen_solidos,volumen_agua,volumen_aire):
    
    if volumen_solidos is None or volumen_agua is None or volumen_aire is None:
        return 'Falta agregar un valor' 
    volumen_solidos = int(volumen_solidos)
    volumen_agua = int(volumen_agua)
    volumen_aire = int(volumen_aire)
    volumen_total = volumen_agua + volumen_aire + volumen_solidos
    encoded_image = fases_del_suelo_vol(volumen_solidos,volumen_agua,volumen_aire)
    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))
    texto = html.H3('El volumen total de la muestra de suelo en m^3 es: ' + str(volumen_total))   
    return html.Div([texto, image_element])



#Datos relación gravimétrica
@app.callback(
    Output('fases_del_suelo_grav', 'children'),
    Input('peso_solidos', 'value'),
    Input('peso_agua', 'value'),
    Input('peso_aire', 'value'),
)    

def peso_total(peso_solidos,peso_agua,peso_aire):
    
    if peso_solidos is None or peso_agua is None or peso_aire is None:
        return 'Falta agregar un valor'
    peso_total = peso_solidos + peso_agua + peso_aire
    encoded_image = fases_del_suelo_grav(peso_solidos,peso_agua,peso_aire)
    image_element2 = html.Img(src="data:image/png;base64,{}".format(encoded_image))
    texto2 = html.H3('El peso total de la muestra de suelo en g es: ' + str(peso_total))
    return html.Div([texto2, image_element2])


if __name__ == '__main__':
    app.run_server(debug=True)

