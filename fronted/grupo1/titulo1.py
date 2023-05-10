from dash import html
import dash_bootstrap_components as dbc


titulo1 = dbc.Container(
    [
        html.H1('VOLUMETRÍA Y GRAVIMETRÍA DE SUELOS'),
        dbc.Row(
        [
            dbc.Col('DEFINICIÓN'),
            dbc.Label('El suelo es un material constituido por partículas sólidas rodeado por espacios libres (vacíos), los cuales generalmente son ocupados por agua o aire'),
            dbc.Col('FASES DEL SUELO'),
            dbc.Label('Sólida: formada por partículas minerales del suelo, incluyendo la capa sólida absorbida.'),
            dbc.Label('Líquida: generalmente agua (específicamente agua libre), aunque pueden existir otros líquidos de menor significancia.'),
            dbc.Label('Gaseosa: comprende todo el aire, el cual puede estar compuesto por vapores de sulfuro, anhídridos carbónicos, etc.'),
        ]
        )
    ]
)

