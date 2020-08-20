from time import sleep

from dash.testing.application_runners import import_app

# The function name follows this pattern: test_{tcid}_{test title}.
# The tcid (test case ID) is an abbreviation pattern of mmffddd => module + file + three digits.
from selenium.webdriver.support.select import Select


def test_dada001_h1textequals(dash_duo):
    app = import_app("single_page_app.app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=4)
    h1_text = dash_duo.find_element("h1").text
    assert h1_text.casefold() == 'Global Covid-19 daily cases'.casefold()


def test_dada002_countrydropdowncontainsworld(dash_duo):
    app = import_app("single_page_app.app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=4)
    assert 'World' in dash_duo.find_element("#country").text, "'World' should appear in the country dropdown"


'''
Write your own test here to assert that when the country dropdown is changed to Andorra that the card title for the 
stats panel is also changed to Andorra.

You will need to use the select_dcc_dropdown function to select an option in the dropdown which has the following 
syntax: 
    select_dcc_dropdown(elem_or_selector, value=None, index=None)
'''
