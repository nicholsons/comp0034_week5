# Introduction to interactivity in Dash

## Recap from last week 
Last week you were introduced to the dash_html_components which you used in the Dash layout.

As a reminder code such as:
```python
import dash_html_components as html

html.Div([
    html.H1('First Dash App'),
    html.Div([
        html.P("Dash converts Python classes into HTML"),
    ])
])
```
Would turn into html as:

```html
  <div>
    <h1>First Dash App/h1>
    <div>
        <p>Dash converts Python classes into HTML</p>
    </div>
</div>
```
You also used the [Graph component](https://dash.plotly.com/dash-core-components/graph) from the dash_core_components library to generate figures. The figures themselves were created using Plotly Express or Plotly Graph Objects and we mostly used pandas dataframes for manipulating the data.

## Focus for this week
This week we are going to look at more [Dash core components](https://dash.plotly.com/dash-core-components). 

We will focus on the Input component and associated callbacks for achieving interaction.

## This activity
### Data
Have a look at `data.py` in the data directory.

This creates a class with the pandas dataframes that we will use in generating the figures.

It is currently reading from data saved in the CSSE_data folder to allow you to run the code without an internet connection. However this data is from August 2020, to get the latest data then replace the DATA_LOC value with the URL to the latest John Hopkins source data.

### Dash App layout
Have a look at `dash.py` and then run it to see the current app.

The app is styled using the dash_bootstrap_components LUX theme ([see list of themes](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/)).

Try out some of the other themes and choose one you like and apply it to the app.

### Set-up the overall page structure using Bootstrap rows and columns
Hopefully you completed the bootstrap activities in week 2. If so you should be familiar with the grid layout that Bootstrap supports.

One of the ways you can define the overall structure with Bootstrap is to divide the page into rows and columns.

For our Covid app we are going to have a single row with two columns.

The first column will contain the country drop down menu and the summary statistics.

The second column will be used to display the chart. The chart area will have two tabs, a different chart will be displayed on each tab.

Modify the app.Layout as follows:

```python
app.layout = dbc.Container(fluid=True, children=[
    html.Br(),
    html.H1('Global Covid-19 daily cases'),
    dbc.Row([
        # Country input and summary statistics panel
        dbc.Col(md=3, children=[
            html.Br(),
            html.P('Placeholder for the stats panel'),
            html.Div(id="output-panel")
        ]),
        # Figures
        dbc.Col(md=9, children=[
            dbc.Col(html.H4("Covid cases"), width={"size": 6, "offset": 3}),
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(dcc.Graph(id="plot-total"), label="Total cases"),
                dbc.Tab(dcc.Graph(id="plot-active"), label="Active cases")
            ])
        ])
    ])
])
```
Now stop and restart the app.

You should see a 2 column layout with empty charts in the centre.

### Add a statistics panel to the dashboard
Let's create the statistics that will be displayed in the summary stats panel.

