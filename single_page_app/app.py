import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from single_page_app.data import Data
from single_page_app.charts import RecyclingChart

# Prepare the data set
data = Data()

# Create the figures
area = 'London'
rc = RecyclingChart(data)
fig1 = rc.create_chart(area)

# Create a Dash app (using bootstrap).
app = dash.Dash(external_stylesheets=[dbc.themes.LITERA])

# Create the app layout using Bootstrap fluid container
app.layout = dbc.Container(fluid=True, children=[
    html.Br(),
    html.H1('Waste and recycling'),
    html.P('Turn London waste into an opportunity – by reducing waste, reusing and recycling more of it.',
           className='lead'),
    html.H2('Recycling'),
    dcc.Graph(figure=fig1)

])

if __name__ == '__main__':
    app.run_server(debug=True)
