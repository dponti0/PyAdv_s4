"""
Script to make updates in GitHub
"""

import click
import pandas as pd

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

@click.command(short_help="Parse and filter dataset")
@click.option("-i", "--input", help="Path to the CSV file", required=True)

def main(input: str):
    """
    Main function to import a dataset and perform filtering by price
    """
    try:
        df = pd.read_csv(input)
        print(f"The file '{input}' was correctly read!")
    except FileNotFoundError:
        print(f"Error: File not found at '{input}'. Provide a valid file path")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: The file at '{input}' is empty")
        return

    # Debugging point
    import pdb; pdb.set_trace()

    # Perform filtering
    filtering_price = 6.50
    result_df = FilteringClass(df).filter_by_price(filtering_price)
    print(f"The filtering price established was: ${filtering_price}")

    # Display the results
    print(f"Original DataFrame Shape: {df.shape}")
    print(f"Filtered DataFrame Shape: {result_df.shape}")

if __name__ == "__main__":
    print("The code is properly working!")
    main()


    # python scripts/repo_first_script.py -i datasets/BooksDatasetClean.csv