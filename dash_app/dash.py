import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from dash_app.chart_creator import ChartCreator
from data.data import Data

# Import the data set
data = Data()

# Create the figures
charts = ChartCreator(data.df)
fig_total = charts.fig_total()
fig_active = charts.fig_active()

# Create a Dash app (using bootstrap).
app = dash.Dash(external_stylesheets=[dbc.themes.LUX])

# Create the app layout using Bootstrap fluid container
app.layout = dbc.Container(fluid=True, children=[
    html.Br(),
    html.H1('Global Covid-19 daily cases')
])
