from dash import html, dcc
import dash_bootstrap_components as dbc


titulo2 = dbc.Container(
    [
        html.Hr(),
        html.Div(
            [
                html.H1("Diagrama de Fases"),
                html.Label("Relación volumétrica (m3)"),
                html.Label("Volumen sólidos (m3)"),
                dcc.Input(id='volumen_solidos', type='number', placeholder='Ejemplo: 100, 150, 200'),
                html.Label("Volumen agua (m3)"),
                dcc.Input(id='volumen_agua', type='number', placeholder='Ejemplo: 100, 150, 200'),
                html.Label("Volumen aire (m3)"),
                dcc.Input(id='volumen_aire', type='number', placeholder='Ejemplo: 100, 150, 200'),
                html.Label("Volumen vacíos (m3)"),
                dcc.Input(id='volumen_vacios', type='number', placeholder='Ejemplo: 100, 150, 200'),
                html.Label("Volumen total (m3)"),
                dcc.Input(id='volumen_total', type='number', placeholder='Ejemplo: 100, 150, 200'),
                html.Button('Generar Diagrama', id='button-generar', n_clicks=0),
                
                html.Label("Relación gravimetrica (g)"),
                html.Label("Peso del agua (g)"),
                dcc.Input(id='peso_agua', type='number', placeholder='Ejemplo: 100, 150, 200'),
                html.Label("Peso de sólidos (g)"),
                dcc.Input(id='peso_solidos', type='number', placeholder='Ejemplo: 100, 150, 200'),
                html.Label("Peso aire (g)"),
                dcc.Input(id='peso_aire', type='number', placeholder='Ejemplo: 100, 150, 200'),
                html.Label("Peso total (g)"),
                dcc.Input(id='peso_total', type='number', placeholder='Ejemplo: 100, 150, 200'),

                html.Button('Generar Diagrama', id='button-generar', n_clicks=0),
                dcc.Graph(id='fases_del_suelo'),
                html.Div(id='fases_del_suelo'),
            ]
        )
    ]
)