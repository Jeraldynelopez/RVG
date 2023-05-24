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
    volumen_total = volumen_agua + volumen_aire + volumen_solidos
    return 'El volumen total de la muestra de suelo en m^3 es: ' + str(volumen_total) 


def fases_del_suelo_volDash(volumen_solidos,volumen_agua,volumen_aire):
    #retrasar la página un segundo
    # time.sleep(1)
    encoded_image = fases_del_suelo_vol(volumen_solidos,volumen_agua,volumen_aire)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))

    return html.Div([image_element])


#Datos relación gravimétrica
@app.callback(
    Output('fases_del_suelo_grav', 'children'),
    Input('peso_solidos', 'value'),
    Input('peso_agua', 'value'),
    Input('peso_aire', 'value'),
)    

def peso_total(peso_solidos,peso_agua,peso_aire):
    peso_total = peso_solidos + peso_agua + peso_aire
    return 'El peso total de la muestra de suelo en gr es: ' + str(peso_total)


def fases_del_suelo_gravDash(peso_solidos,peso_agua,peso_aire):
    #retrasar la página un segundo
    # time.sleep(1)
    encoded_image = fases_del_suelo_grav(peso_solidos,peso_agua,peso_aire)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))

    return html.Div([image_element])

if __name__ == '__main__':
    app.run_server(debug=True)

