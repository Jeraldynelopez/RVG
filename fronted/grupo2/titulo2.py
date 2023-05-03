from dash import html
import dash_bootstrap_components as dbc

titulo2 = dbc.Container(
    [
        html.H1('Datos o entradas iniciales')
        html.Hr()
        html.label('Volumen a calcular')
        dcc.Dropdown(
            ['Vs-Volumen de sólidos', 'Vv-Volumen de vacios', 'Vw-Volumen de agua', 'Vt-Volumen total'],
        )
        html.label('Peso a calcular')
        dcc.Dropdown(
            ['Ws-Peso solidos', 'Ww-Peso de agua', 'Wt-Peso total'],
        )
    ]
)
