from dash import html
import dash_bootstrap_components as dbc


titulo1 = dbc.Container(
    [
        html.Hr(),
        html.H1('VOLUMETRÍA Y GRAVIMETRÍA DE SUELOS'),
        html.Hr(),
        dbc.Row(
        [
            dbc.Col('DEFINICIÓN', md=12, style={'background-color':'Darkgray'}),
            dbc.Label('El suelo es un material constituido por partículas sólidas rodeado por espacios libres (vacíos), los cuales generalmente son ocupados por agua o aire.', md=12, style={'background-color':'Gainsboro'}),
            dbc.Col('FASES DEL SUELO', md=12, style={'background-color':'Darkgray'}),
            dbc.Label('Sólida: formada por partículas minerales del suelo, incluyendo la capa sólida absorbida.', md=12, style={'background-color':'Gainsboro'}),
            dbc.Label('Líquida: generalmente agua (específicamente agua libre), aunque pueden existir otros líquidos de menor significancia.', md=12, style={'background-color':'Gainsboro'}),
            dbc.Label('Gaseosa: comprende todo el aire, el cual puede estar compuesto por vapores de sulfuro, anhídridos carbónicos, etc.', md=12, style={'background-color':'Gainsboro'}),
        ]
        ),
        html.Hr(),
    ]
)

