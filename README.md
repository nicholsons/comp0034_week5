# COMP0034 Week 4 course material

This a repository of materials that support the Moodle activities for week 4. It is not intended for use as a standalone repository.

The data is from the [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19) as at 17th August 2020.

The exercises in this week make use of the dash-bootstrap-components library.

The exercises were inspired by, and use and adapt code from, the article [How to embed Bootstrap CSS & JS in your Python Dash app](https://towardsdatascience.com/how-to-embed-bootstrap-css-js-in-your-python-dash-app-8d95fc9e599e). The article also uses machine learning to forecast which we are not covering in this course.

## Setup
- Create a venv: `python -m venv venv`
- Install the requirements in the venv: `pip install -r requirements.txt`

## Directory structure
```
/dash_app/ # Directory for the dash app
    assets/
    dash.py  # Dash app code
/data/ # Data Python module
    CSSE_data/  # Data downloaded from John Hopkins as at 17/08/20
    data.py  # Python class to represent the data
/exercises/ # Directory of instructions for the Moodle activities
.gitignore # Standard Python and JetBrains (PyCharm) ignored files for git
requirements.txt # The dependant libraries for the exercises
```