from dash import html, dcc
import dash_bootstrap_components as dbc

titulo2 = dbc.Container(
    [
        html.H1('Entradas iniciales'),
        html.Hr(),
        html.Label('Volumen a calcular'),
        dcc.Dropdown(
            ['Vs-Volumen de sólidos', 'Vv-Volumen de vacios', 'Vw-Volumen de agua', 'Vt-Volumen total'],
        ),
        html.Label('Peso a calcular'),
        dcc.Dropdown(
            ['Ws-Peso solidos', 'Ww-Peso de agua', 'Wt-Peso total'],
        )
    ]
)
