from dash import html, dcc
import dash_bootstrap_components as dbc


#import fronted
from fronted.grupo1.titulo1 import titulo1
from fronted.grupo2.titulo2 import titulo2
from fronted.grupo3.titulo3 import titulo3


layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(titulo1, md=12, style={'background-color':'white'}),
                dbc.Col(titulo2, md=8, style={'background-color':'blue'}),
                dbc.Col(titulo3, md=4, style={'background-color':'gray'}),

            ]
        )
    ]
)
