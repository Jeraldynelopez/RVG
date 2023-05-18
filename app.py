import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import math
import time

#import fronted
from fronted.main import layout
from backend.fases_del_suelo import *

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout

#Datos relación volumétrica
@app.callback(
    Output('fases_del_suelo_vol', 'children'),
    Input('volumen_solidos', 'value'),
    Input('volumen_agua', 'value'),
    Input('volumen_aire', 'value'),
    Input('volumen_total', 'value'),
)

#Datos relación gravimétrica
@app.callback(
    Output('fases_del_suelo_grav', 'children'),
    Input('peso_solidos', 'value'),
    Input('peso_agua', 'value'),
    Input('peso_aire', 'value'),
    Input('peso_total', 'value'),
)

def fases_del_suelo_volDash(volumen_solidos,volumen_agua,volumen_aire,volumen_total):
    #retrasar la página un segundo
    # time.sleep(1)
    encoded_image = fases_del_suelo_vol(volumen_solidos,volumen_agua,volumen_aire,volumen_total)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))

    return html.Div([image_element])

def fases_del_suelo_gravDash(peso_solidos,peso_agua,peso_aire,peso_total):
    #retrasar la página un segundo
    # time.sleep(1)
    encoded_image = fases_del_suelo_grav(peso_solidos,peso_agua,peso_aire,peso_total)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))

    return html.Div([image_element])

if __name__ == '__main__':
    app.run_server(debug=True)

