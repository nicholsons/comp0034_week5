# Introduction to interactivity in Dash

Watch the video: TO BE RECORDED

This activity is also documented in the [GitHub repository](https://github.com/nicholsons/comp0034_week4.git) in `exercises/1_dash_interactivity_intro.md`

## So far
Last week you were introduced to the basic structure of a dash app which looked something like this:
```python
# Import the required libraries.
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Import the data set
df = pd.read_csv(path_to_csv_file)

# Create the Plotly figure 
fig = px.bar(df, x="spend", y="date", color="place", title="Purchases by place")

# Create a Dash app
app = dash.Dash(__name__)

# Create the app layout
app.layout = html.Div(children=[
    html.H1('My heading'),
    dcc.Graph(figure=fig)
])

# Run the web app server
if __name__ == '__main__':
    app.run_server(debug=True)

```

You used the dash_html_components to define a static layout in the app.layout. 

Code such as:
```python
import dash_html_components as html

html.Div([
    html.H1('First Dash App'),
    html.Div([
        html.P("Dash converts Python classes into HTML"),
    ])
])
```
would turn into html as:
```html
  <div>
    <h1>First Dash App/h1>
    <div>
        <p>Dash converts Python classes into HTML</p>
    </div>
</div>
```
You also used the [Graph component](https://dash.plotly.com/dash-core-components/graph) from the dash_core_components library to generate figures. The figures themselves were created using Plotly Express or Plotly Graph Objects and we mostly used pandas dataframes for manipulating the data.

## Introduction to this activity

In this activity we are going to look at more [Dash core components](https://dash.plotly.com/dash-core-components) and the use of callbacks for achieving interaction.

If you have not already, then fork or clone the [GitHub repository](), create a venv and install the libraries from requirements.txt.

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
            dbc.FormGroup([
                html.H4("Select Country"),
                dcc.Dropdown(id="country", options=[{"label": x, "value": x} for x in data.country_list], value="World")
            ]),
            html.Br(),
            html.Div(id="output-panel")
        ]),
        # Figures
        dbc.Col(md=9, children=[
            dbc.Col(html.H4("Covid cases"), width={"size": 6, "offset": 3}),
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(dcc.Graph(id="fig-total", figure=fig_total), label="Total cases"),
                dbc.Tab(dcc.Graph(id="fig-active", figure=fig_active), label="Active cases")
            ])
        ])
    ])
])
```
Now stop and restart the app.

You should see a 2 column layout with charts accessed using tabs.

While you can use the country selector drop down, nothing happens when you select a country.

### Add a callback so that the statistics panel is displayed when a country is selected

A callback function is a Python function that is automatically called by Dash whenever an input component's property changes.

The basic structure of the callback is:

`@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='my-input', component_property='value')]
)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)`

- By writing this decorator, we're telling Dash to call this function for us whenever the value of the "input" component (the text box) changes in order to update the children of the "output" component on the page (the HTML div).
- You can use any name for the function that is wrapped by the @app.callback decorator. The convention is that the name describes the callback output(s).
- You can use any name for the function arguments, but you must use the same names inside the callback function as you do in its definition, just like in a regular Python function. The arguments are positional: first the Input items and then any State items are given in the same order as in the decorator.
- You must use the same id you gave a Dash component in the app.layout when referring to it as either an input or output of the @app.callback decorator.
- The @app.callback decorator needs to be directly above the callback function declaration. If there is a blank line between the decorator and the function definition, the callback registration will not be successful.

To create a callback we need to:

- Define the Input: identify the component id (e.g. id of an html element) and component property that the user will interact with
- Define the Outputs: identify the component id and property that will be updated after we make a change
- Write a Python function using the @callback decorator. The function will be run when the Input has been selected

To display the statistics panel when the country dropdown selection is changed we need to:

- Input: If you look at the first column in our app layout you should see the form we created for the dropdown. The dropdown has an `id=country'` and the item that is selected from the list is the `value=` parameter.
The Input functionality is a class provided in the dash.dependencies module so we will need the import `from dash.dependencies import Output, Input`.
So, we can reference the country that is selected as `Input("country","value")`

- Outputs: The last line of the first column in the app layout added a placeholder div: `html.Div(id="output-panel")`.
We want to output a Bootstrap card with the statistics in and place it in this div, that is the card becomes the `children=` of the `html.Div(id="output-panel")`.
So, we can reference the div as our output as `Output("output-panel","children")`.

- Callback function
The function will take the country name selected in the dropdown and process the data for that country.
Once the data has been processed the stats can be generate by the result object.
The stats generated by the `results.get_stats()` method are then used to generate a bootstrap styled card with the statistical summary data.
The HTML page is then updated by passing this 'card' to the div with the id of `"output-panel"`.

The code to do this is as follows. Copy and paste this into the end of `dash.py` and then restart the app.

The summary stats should change as the country is changed. The next step will be to change the charts when the stats are updated.

```python
@app.callback(Output("output-panel", "children"), [Input("country", "value")])
def render_output_panel(country):
    data.process_data(country)
    result = Result(data.df)
    peak_day, num_max, total_cases_until_today, active_cases_today = result.get_stats()
    panel = html.Div([
        html.H4(country),
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
            html.H6("with {:,.0f} cases".format(num_max), className="card-title text-light" ),
            html.Br()
        ])
    ])
    return panel
```
### Update the charts when a country is selected
Now it is over to you, see if you can add two further callbacks to dash.py:

1. Add a plot_total_cases(country) callback that takes the same input as the stats panel and outputs to the chart component with the fig_total id.
The function takes the country, processes the data for that country, creates a new result object and calls the appropriate method to generate the total cases figure.

2. Repeat for the plot_active_cases(country) callback.
