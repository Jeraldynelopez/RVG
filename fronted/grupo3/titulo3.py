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
        html.H2('Diagrama suelo seco'),
        html.Img(src=ruta_imagen_seco, style={'max-width': '100%'}),
        html.H3('Diagrama suelo saturado'),
        html.Img(src=ruta_imagen_saturado, style={'max-width': '100%'}),
        html.H4('Diagrama suelo humedo'),
        html.Img(src=ruta_imagen_humedo, style={'max-width': '100%'}),
    ]
)