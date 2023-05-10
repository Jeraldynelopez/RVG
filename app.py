import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import math
import time

#import fronted
from fronted.main import layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout



if __name__ == '__main__':
    app.run_server(debug=True)

