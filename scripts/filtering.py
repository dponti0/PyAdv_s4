"""
All the filters for the dataset
"""

# Import the needed libraries
import pandas as pd

# Elaborate on the filter class
class FilteringClass:
    """
    Class for filtering operations on a DataFrame
    """
    def __init__(self, df: pd.DataFrame):
        """
        Initialize the class with a DataFrame
        """
        self.df = df

    def filter_by_price(self, min_price: float) -> pd.DataFrame:
        """
        Filter the DataFrame based on the minimum price
        """
        return self.df[self.df["Price Starting With ($)"] > min_price]

    def filter_by_publish_date(self, year: int, month: int) -> pd.DataFrame:
        """
        Filter the DataFrame based on the publish date (year and month)
        """
        return self.df[(self.df["Publish Date (Year)"] == year) & (self.df["Publish Date (Month)"] == month)]
    
    def filter_by_description_length(self, min_length: int) -> pd.DataFrame:
        """
        Filter the DataFrame based on the length of the description
        """
        return self.df[self.df["Description"].str.len() > min_length]
    
    def filter_title_starting_with_vowel(self) -> pd.DataFrame:
            """
            Filter the DataFrame based on titles starting with a vowel
            """
            vowels = ['a', 'e', 'i', 'o', 'u']
            return self.df[self.df['Title'].str[0].str.lower().isin(vowels)]
    
    def filter_by_category(self, category: str) -> pd.DataFrame:
        """
        Filter the DataFrame based on the category
        """
        return self.df[self.df["Category"].str.contains(category, case=False, na=False)]