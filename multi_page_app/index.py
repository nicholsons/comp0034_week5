import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from multi_page_app.apps.app1 import app1
from multi_page_app.apps.app2 import app2

from multi_page_app.app import app

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_layout = html.Div([
    html.P('Hello')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/app1':
        return app1.layout
    elif pathname == '/app2':
        return app2.layout
    elif pathname == '/':
        return index_layout
    else:
        return '404 Page Not Found'


if __name__ == '__main__':
    app.run_server(debug=True)