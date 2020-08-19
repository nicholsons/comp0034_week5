# Introduction to interactivity in Dash

Watch the video: TO BE RECORDED

This activity is also documented in the [GitHub repository](https://github.com/nicholsons/comp0034_week4.git) in `exercises/2_multi_page_dash_app.md`

You will likely need to refer to the [Multi page apps and URL support](https://dash.plotly.com/urls) in the Dash documentation.

## Introduction to this activity
In the last activity you learned how to use callbacks to add interactivity to your dash application.

In the app layout you added the two charts using tabs, however the app itself was still a single page app.

This activity will introduce you to creating a multi-page Dash app.

## File structure for a multi page app
Plotly recommends either:
1. Each app is contained in a separate file
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
The latter is consistent with the approach taken in the first activity to separate different data preparation, chart creation and app creation into separate files.

The above files will be created in the `dash_app` folder. The contents from current dash.py will be separated into the relevant files and we will ignore dash.py for this exercise.
