from dash import html
import dash_bootstrap_components as dbc

titulo1 = dbc.Container(
    [
        html.H1('VOLUMETRÍA Y GRAVIMETRÍA DE SUELOS')
        dbc.Row(
        [
            dbc.Col('Definición')
            dbc.Col('Datos')
        ]
        )
    ]
)