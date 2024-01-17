"""
Script to make updates in GitHub
"""

# Importing the libraries
import sys
import click
import pandas as pd
sys.path.append("scripts")
from filtering import FilteringClass

def load_dataset(filename):
    """
    Function to load the dataset
    """
    extension = filename.rsplit(".",1)[-1]
    if extension=="csv":
        return pd.read_csv(filename)
    raise TypeError(f"The extension is {extension} ad not a csv. Try again.")

@click.command(short_help="Parse and filter dataset")
@click.option("-i", "--input", help="Path to the CSV file", required=True)
@click.option("-p", "--price", type=float, help="Filter by minimum price")
@click.option("-c", "--category", help="Filter by category")
@click.option("-y", "--year", type=int, help="Filter by publish year")
@click.option("-m", "--month", help="Filter by publish month")

def main(input: str, price: float, category: str, year: int, month: int):
    """
    Main function to import a dataset and perform filtering operations
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
    if price is not None:
        result_df_price = FilteringClass(df).filter_by_price(price)
        print(f"The filtering price established was: ${price}")
    else:
        result_df_price = df

    if category is not None:
        result_df_category = FilteringClass(df).filter_by_category(category)
        print(f"The filtering category established was: {category}")
    else:
        result_df_category = df

    if year is not None and month is not None:
        result_df_publish_date = FilteringClass(df).filter_by_publish_date(year, month)
        print(f"The filtering publish date established was: {year}-{month}")
    else:
        result_df_publish_date = df

    # Display the results
    print(f"Original DataFrame Shape: {df.shape}")
    print(f"Filtered DataFrame by Price Shape: {result_df_price.shape}")
    print(f"Filtered DataFrame by Category Shape: {result_df_category.shape}")
    print(f"Filtered DataFrame by Publish Date Shape: {result_df_publish_date.shape}")

if __name__ == "__main__":
    print("The code is properly working!")
    main()


    # python scripts/repo_first_script.py -i datasets/BooksDatasetClean.csv -p 6.50 -c Fiction -y 1995 -m January