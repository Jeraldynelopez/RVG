from dash import html, dcc
import dash_bootstrap_components as dbc
import time
import math


titulo2 = dbc.Container(
    [
        html.Div(
            [
                html.H1("Datos"),
                html.H2("Relación volumétrica (m3): "),
                html.Br(),
                html.Label("Volumen sólidos (m3):"),
                dcc.Input(id='volumen_solidos', type='number', placeholder='Ejemplo: 100, 150, 200'),
                html.Br(),
                html.Label("Volumen agua (m3):"),
                dcc.Input(id='volumen_agua', type='number', placeholder='Ejemplo: 100, 150, 200'),
                html.Br(),
                html.Label("Volumen aire (m3):"),
                dcc.Input(id='volumen_aire', type='number', placeholder='Ejemplo: 100, 150, 200'),
                html.Br(),
                #html.Label("Volumen vacíos (m3):"),
                #dcc.Input(id='volumen_vacios', type='number', placeholder='Ejemplo: 100, 150, 200'),
                #html.Br(),
                #html.Label("Volumen total (m3):"),
                #html.Label(id='volumen_total'),
                #html.Br(),
                #html.Button('Generar Diagrama', id='button-generar', n_clicks=0),
                #html.Br(),
                #html.Hr(),
                #dcc.Graph(id='fases_del_suelo_vol'),
                html.Div(id='fases_del_suelo_vol')
                #html.Hr(),
            ],
        ),

        html.Hr(),

        html.Div(
            [
                html.H3("Relación gravimétrica (g):"),
                html.Br(),
                html.Label("Peso del agua (g):"),
                dcc.Input(id='peso_agua', type='number', placeholder='Ejemplo: 100, 150, 200'),
                html.Br(),
                html.Label("Peso de sólidos (g):"),
                dcc.Input(id='peso_solidos', type='number', placeholder='Ejemplo: 100, 150, 200'),
                html.Br(),
                html.Label("Peso aire (g):"),
                dcc.Input(id='peso_aire', type='number', placeholder='Ejemplo: 0'),
                html.Br(),
                #html.Label("Peso total (g):"),
                #html.Label(id='peso_total'),
                #html.Br(),
                #html.Button('Generar Diagrama', id='button-generar', n_clicks=0),
                #html.Hr(),
                #dcc.Graph(id='fases_del_suelo'),
                html.Div(id='fases_del_suelo_grav')
                #html.Hr(),
            ]
        )
    ]
)