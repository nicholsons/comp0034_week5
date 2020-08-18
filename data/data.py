import os

import pandas as pd


class Data:
    """Class for retrieving and structuring the Covid global time series data of daily cases."""

    def __init__(self):
        self.cases = []
        self.country_list = []
        self.df = []
        self.today = ''
        self.get_data()
        self.process_data('World')

    def get_data(self):
        # Replace the local file with the URL in DATA_LOC to get the latest cases
        # DATA_LOC = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data
        # /csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
        DATA_DIR = os.path.join(os.getcwd(), 'data/CSSE_data')
        DATA_LOC = os.path.join(DATA_DIR, 'time_series_covid19_confirmed_global.csv')
        self.cases = pd.read_csv(DATA_LOC, sep=",")
        self.cases = self.cases.drop(['Province/State', 'Lat', 'Long'], axis=1)
        self.country_list = ["World"] + self.cases["Country/Region"].unique().tolist()

    def process_data(self, country):
        self.df = self.group_by_country(self.cases, country)
        self.df["delta_data"] = self.df["data"] - self.df["data"].shift(1)
        self.today = self.df.index[-1]

    @staticmethod
    def group_by_country(df, country):
        # Group by Country and transpose the data
        df = df.groupby("Country/Region").sum().T
        df["World"] = df.sum(axis=1)
        df = df[country]
        df.index = pd.to_datetime(df.index, infer_datetime_format=True)
        ts = pd.DataFrame(index=df.index, data=df.values, columns=["data"])
        return ts
