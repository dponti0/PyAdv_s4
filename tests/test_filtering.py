"""
Test filtering code
"""

# Import the necessary libraries
import pandas as pd
import unittest
from scripts.filtering import FilteringClass

# Define the class
class TestFiltering(unittest.TestCase):
    """
    Class to test the filters on the dataset
    """
    
    def setUp(self) -> None:
        # Load the DataFrame from the CSV file
        self.path = "datasets/BooksDatasetClean.csv"
        self.df = pd.read_csv(self.path)

    def test_filtering_price(self):
        # Test filtering by price
        min_price = 18.0
        filtered_df = FilteringClass(self.df).filter_by_price(min_price)
        expected_result = self.df[self.df["Price Starting With ($)"] > min_price]
        self.assertTrue(filtered_df.equals(expected_result))

    def test_filter_by_publish_date(self):
            # Test filtering by publish date
            year = 2022
            month = 1

            filtering_instance = FilteringClass(self.df)

            # Perform filtering
            filtered_df = filtering_instance.filter_by_publish_date(year, month)

            # Print the results for debugging
            print("Original DataFrame Shape:", self.df.shape)
            print("Filtered DataFrame Shape (Publish Date Filter):", filtered_df.shape)

    def test_filtering_category(self):
        # Test filtering by category containing "Fiction"
        category = 'Fiction'
        filtered_df = FilteringClass(self.df).filter_by_category(category)
        expected_result = self.df[self.df["Category"].str.contains(category, case=False, na=False)]
        self.assertTrue(filtered_df.equals(expected_result))

    def test_filtering_description_length(self):
        # Test filtering by description length
        min_length = 5
        filtered_df = FilteringClass(self.df).filter_by_description_length(min_length)
        expected_result = self.df[self.df["Description"].str.len() > min_length]
        self.assertLessEqual(filtered_df.shape[0], self.df.shape[0])  # Assert that the resulting DataFrame has fewer or equal rows

    def test_filter_title_starting_with_vowel(self):
        # Test filtering based on titles starting with a vowel
        filtering_instance = FilteringClass(self.df)

        # Perform filtering
        filtered_df = filtering_instance.filter_title_starting_with_vowel()

        # Print the results for debugging
        print("Original DataFrame Shape:", self.df.shape)
        print("Filtered DataFrame Shape (Title Starting with Vowel):", filtered_df.shape)

        # Ensure the result DataFrame is not empty
        self.assertFalse(filtered_df.empty)

if __name__ == "__main__":
    unittest.main()
