import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


# Importar componentes de título
from fronted.grupo1.titulo1 import titulo1
from fronted.grupo2.titulo2 import titulo2
from fronted.grupo3.titulo3 import titulo3

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(titulo1, md=12, style={'background-color': 'rgba(255, 255, 255, 0.5)'}),
                dbc.Col(titulo2, md=8, style={'background-color': 'rgba(0, 0, 255, 0.5)'}),
                dbc.Col(titulo3, md=4, style={'background-color': 'rgba(128, 128, 128, 0.5)'}),
            ]
        )
    ]
)



if __name__ == "__main__":
    app.run_server(debug=True)