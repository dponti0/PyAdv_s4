"""
All the filters for the dataset
"""

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

    def filter_by_category(self, category: str) -> pd.DataFrame:
        """
        Filter the DataFrame based on the category
        """
        return self.df[self.df["Category"] == category]

    def filter_by_publish_date(self, year: int, month: int) -> pd.DataFrame:
        """
        Filter the DataFrame based on the publish date (year and month)
        """
        return self.df[(self.df["Publish Date (Year)"] == year) & (self.df["Publish Date (Month)"] == month)]