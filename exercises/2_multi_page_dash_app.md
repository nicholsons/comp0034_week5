# Creating a multi page Dash app

You will likely need to refer to the [Multi page apps and URL support](https://dash.plotly.com/urls) in the Dash documentation.

## Introduction to this activity
In the last activity you learned how to use callbacks to add interactivity to your dash application.

If you complete the final challenge then you may have added two charts using tabs, however the app itself was still a single page app.

This activity will introduce you to creating a multi-page Dash app.

The code for this activity is withing the `multi_page_app` directory.

## File structure for a multi page app
Plotly recommends either:
1. Each app is contained in a separate file (or directory)
```
- app.py
- index.py
- apps
   |-- __init__.py
   |-- app1.py
   |-- app2.py
```
or
2. a flat project layout with callbacks and layouts separated into different files:
```
- app.py
- index.py
- callbacks.py
- layouts.py
```
For this activity we will take the first approach.

The app from first exercise has been copied into the multi_page_app directory just to keep the files for each activity separate.

In both of these project structures, the Dash instance is defined in a separate app.py, while the entry point for running the app is index.py. 
This separation is required to avoid circular imports: the files containing the callback definitions require access to the Dash app instance however if this were imported from index.py, the initial loading of index.py would ultimately require itself to be already imported, which cannot be satisfied.

### app.py
This file defines the Dash instance. In this example we are also applying the Dashboot-bootstrap-component LUX template to provide consistent styling for the apps.

### index.py
This file both defines the routing for the app and a layout for the index page (layout is optional).

The routing, i.e. which app to display when a given url is entered, is defined in the `display_page` callback.

`app.layout` provides a sort of template for pages in the app.

### app1.py
This is the recycling dashboard app from the previous activity. The changes are:
- app is created in app.py and is added as an import and the previous code to create the app in app1.py has been deleted

## TASK: Create a navigation bar
Refer to the [Dash bootstrap components documentation for nav bar](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/) for more options and alternatives.

Using bootstrap styling the following code would create a navbar:
```python
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="/app1"), id="page-1-link"),
        dbc.NavItem(dbc.NavLink("Page 2", href="/app2"), id="page-2-link"),
        dbc.NavItem(dbc.NavLink("Page 3", href="/app3"), id="page-3-link")
    ],
    brand="Multi page app example",
    brand_href="/",
    color="primary",
    dark=True,
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])
```

We don't want to duplicate the code on every page so add define the variable `navbar` and add the navbar code such as the above to the app.py.

Anything that you add to app.layout will be visible on every page. The above places the navbar before the main page content i.e. at the top of the page.

Stop and restart the app. You should now have a multipage app.

## TASK: Add a third app
Create a new app called app3.

You can create your own or copy one of the [sample apps in the Dash repository on GitHub](https://github.com/plotly/dash-sample-apps).

Add a link to the `index.py` for app3.
