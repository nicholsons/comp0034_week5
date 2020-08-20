import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from multi_page_app.app import app
from multi_page_app.apps.app1.chart_creator import ChartCreator
from data.data import Data

# Import the data set
data = Data()

# Create the Plotly figures
charts = ChartCreator(data.df)
fig_total = charts.fig_total()
fig_active = charts.fig_active()

# Create a Dash app (using bootstrap).
# app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
# Code removed and instead we use the import: from multi_page_app.app import app

# Create the app layout
# app.layout = dbc.Container(fluid=True, children=[
# app.layout is defined in index.html, we replace the above line with the following line
layout = dbc.Container(fluid=True, children=[
    html.Br(),
    html.H1('Global Covid-19 daily cases'),
    dbc.Row([
        dbc.Col(md=3, children=[
            dbc.FormGroup([
                html.H4("Select Country"),
                dcc.Dropdown(id="country", options=[{"label": x, "value": x} for x in data.country_list], value="World")
            ]),
            html.Br(),
            html.Div(id="output-panel")
        ]),
        dbc.Col(md=9, children=[
            dbc.Col(html.H4("Covid cases"), width={"size": 6, "offset": 3}),
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(dcc.Graph(id="fig-total", figure=fig_total), label="Total cases"),
                dbc.Tab(dcc.Graph(id="fig-active", figure=fig_active), label="Active cases")
            ])
        ])
    ])
])


@app.callback(Output("output-panel", "children"), [Input("country", "value")])
def render_output_panel(country):
    data.process_data(country)
    charts = ChartCreator(data.df)
    peak_day, num_max, total_cases_until_today, active_cases_today = charts.get_stats()
    panel = html.Div([
        html.H4(country, id="card_name"),
        dbc.Card(body=True, className="bg-dark text-light", children=[
            html.Br(),
            html.H6("Total cases until today:", className="card-title"),
            html.H3("{:,.0f}".format(total_cases_until_today), className="card-text text-light"),
            html.Br(),
            html.H6("Active cases today:", className="card-title"),
            html.H3("{:,.0f}".format(active_cases_today), className="card-text text-light"),
            html.Br(),
            html.H6("Peak day:", className="card-title"),
            html.H3(peak_day.strftime("%d-%m-%Y"), className="card-text text-light"),
            html.H6("with {:,.0f} cases".format(num_max), className="card-title text-light"),
            html.Br()
        ])
    ])
    return panel


@app.callback(Output("fig-total", "figure"), [Input("country", "value")])
def plot_total_cases(country):
    data.process_data(country)
    charts = ChartCreator(data.df)
    return charts.fig_total()


@app.callback(Output("fig-active", "figure"), [Input("country", "value")])
def plot_active_cases(country):
    data.process_data(country)
    charts = ChartCreator(data.df)
    return charts.fig_active()
