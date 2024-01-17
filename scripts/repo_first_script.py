"""
Script to make updates in GitHub
"""

# Importing the libraries
import sys
import click
import pandas as pd
sys.path.append("scripts")
from filtering import FilteringClass

# Loading the dataset (function)
def load_dataset(filename):
    """
    Function to load the dataset
    """
    extension = filename.rsplit(".", 1)[-1]
    if extension.lower() != "csv":
        raise TypeError(f"The extension is {extension} and not 'csv'. Try again.")
    return pd.read_csv(filename)

# Click commands
@click.command(short_help="Parse and filter dataset")
@click.option("-i", "--input", help="Path to the CSV file", required=True)
@click.option("-p", "--price", type=float, help="Filter by minimum price")
@click.option("-c", "--category", help="Filter by category")
@click.option("-y", "--year", type=int, help="Filter by publish year")
@click.option("-m", "--month", help="Filter by publish month")

# Defining the main function
def main(input: str, price: float, category: str, year: int, month: int):
    """
    Main function to import a dataset and perform filtering operations
    """
    # Try & except (loading the dataset)
    try:
        df = load_dataset(input)
        print(f"The file '{input}' was correctly read!")

    except FileNotFoundError:
        print(f"Error: File not found at '{input}'. Provide a valid file path")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: The file at '{input}' is empty")
        return

    # Debugging point 
    import pdb; pdb.set_trace()

    # Perform filtering by price
    if price is not None:
        result_df_price = FilteringClass(df).filter_by_price(price)
        print(f"The filtering price established was: ${price}")
    else:
        result_df_price = df

    # Perform filtering by category
    if category is not None:
        result_df_category = FilteringClass(df).filter_by_category(category)
        print(f"The filtering category established was: {category}")
    else:
        result_df_category = df

    # Perform filtering by date
    if year is not None and month is not None:
        result_df_publish_date = FilteringClass(df).filter_by_publish_date(year, month)
        print(f"The filtering publish date established was: {year}-{month}")
    else:
        result_df_publish_date = df

    # Filter titles starting with a vowel
    result_df_vowel_title = FilteringClass(df).filter_title_starting_with_vowel()

    # Filter by description length (50)
    result_df_description_length = FilteringClass(df).filter_by_description_length(50)

    # Display the results
    print(f"Original DataFrame Shape: {df.shape}")
    print(f"Filtered DataFrame by Price Shape: {result_df_price.shape}")
    print(f"Filtered DataFrame by Category Shape: {result_df_category.shape}")
    print(f"Filtered DataFrame by Publish Date Shape: {result_df_publish_date.shape}")
    print("Filtered DataFrame by Titles Starting with a Vowel Shape:", result_df_vowel_title.shape)
    print("Filtered DataFrame by Description Length Shape:", result_df_description_length.shape)

if __name__ == "__main__":
    print("The code is properly working!")
    main()


    # python scripts/repo_first_script.py -i datasets/BooksDatasetClean.csv -p 6.50 -c Fiction -y 1995 -m January