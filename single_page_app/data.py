import pandas as pd

from single_page_app.charts import RecyclingChart


class Data:
    """Class for retrieving and structuring the data.
    TODO: Add error handling for file read issues."""

    def __init__(self):
        self.recycling = pd.DataFrame()
        self.recycling_area = []
        self.recycling_eng = []
        self.area_list = []
        self.get_data()
        self.process_data_for_area('England')

    def get_data(self):
        self.recycling = pd.read_csv('data/household_recycling.csv')
        self.area_list = self.recycling["Area"].unique().tolist()
        self.recycling_eng = self.process_data_for_area('England')

    def process_data_for_area(self, area):
        self.recycling_area = self.recycling.loc[self.recycling['Area'] == area]
        return self.recycling_area
