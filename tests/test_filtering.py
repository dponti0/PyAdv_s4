import pandas as pd
import unittest
from scripts.filtering import FilteringClass

class TestFiltering(unittest.TestCase):
    """
    Class to test the filters on the dataset
    """
    
    def test_filtering_price(self):
        # Test filtering by price
        min_price = 18.0
        filtered_df = FilteringClass(self.df).filter_by_price(min_price)
        expected_result = self.df[self.df["Price Starting With ($)"] > min_price]
        self.assertTrue(filtered_df.equals(expected_result))

    def test_filtering_category(self):
        # Test filtering by category
        category = 'Science'
        filtered_df = FilteringClass(self.df).filter_by_category(category)
        expected_result = self.df[self.df["Category"] == category]
        self.assertTrue(filtered_df.equals(expected_result))

    def test_filtering_publish_month(self):
        # Test filtering by publish month
        month = 2
        filtered_df = FilteringClass(self.df).filter_by_publish_month(month)
        expected_result = self.df[self.df["Publish Date (Month)"] == month]
        self.assertTrue(filtered_df.equals(expected_result))

    def test_combined_filters(self):
        # Test combining multiple filters
        min_price = 15.0
        category = 'Science'
        filtered_df = FilteringClass(self.df).filter_by_price(min_price).filter_by_category(category)
        expected_result = self.df[(self.df["Price Starting With ($)"] > min_price) & (self.df["Category"] == category)]
        self.assertTrue(filtered_df.equals(expected_result))

if __name__ == "__main__":
    unittest.main()
