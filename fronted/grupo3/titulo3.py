import dash
from dash import html
import dash_bootstrap_components as dbc
from PIL import Image


ruta_imagen_seco = Image.open('imagenes\seco.png')
ruta_imagen_saturado = Image.open('imagenes\saturado.png')
ruta_imagen_humedo = Image.open('imagenes\humedo.png')

titulo3 = dbc.Container(
    [
        html.H1('Diagrama de fases del suelo'),
        html.Hr(),
        html.H2('Suelo seco'),
        html.Img(src=ruta_imagen_seco, style={'max-width': '100%'}),
        html.Hr(),
        html.H3('Suelo saturado'),
        html.Img(src=ruta_imagen_saturado, style={'max-width': '100%'}),
        html.Hr(),
        html.H4('Suelo humedo'),
        html.Img(src=ruta_imagen_humedo, style={'max-width': '100%'}),
    ]
)