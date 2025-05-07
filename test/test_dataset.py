import unittest
import pandas as pd
from clean import clean_data

class DataFrameTest(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv("data/data13_small.csv")

    def test_dataset(self):
        self.assertTrue(self.df.shape[0] == 1000000)
        self.assertTrue(self.df.shape[1] == 30)

    def test_data_clean(self):
        self.df = clean_data.clean(self.df)
        self.assertTrue(self.df.shape[0] == 1000000)
        self.assertTrue(self.df.shape[1] == 23)
        self.assertEqual(self.df["birth_date"].dtype, "datetime64[ns]")
        self.assertEqual(self.df["hire_date"].dtype, "datetime64[ns]")
        self.assertEqual(self.df["last_review_date"].dtype, "datetime64[ns]")
        self.assertEqual(self.df.duplicated().sum(), 0)

        columns =  ["days_service", "base_salary", "bonus_percentage", "performance_score", 
                "vacation_days", "sick_days"]

        for column in columns:
            self.assertEqual(self.df[self.df[column] < 0].shape[0], 0)
