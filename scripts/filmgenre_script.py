# Exercise -> FilmGenreStats script

"""
Script to make updates in GitHub
"""

# Import library
import os
import click
import pandas as pd

class FilteringClass:
    """
    Class for filtering operations on a DataFrame
    """
    def __init__(self, df):
        """
        Initialize the class with a DataFrame
        """
        self.df = df

    def filter_by_genre(self, genre):
        """
        Filter the DataFrame based on a specified genre
        """
        return self.df[self.df["Genre"] == genre]

    def filter_by_year(self, year):
        """
        Filter the DataFrame based on a minimum specified year
        """
        return self.df[self.df["Year"] > int(year)]

# Click commands
@click.command(short_help="Parse and filter dataset")
@click.option("-i", "--input", help="Path to the CSV file", required=True)
@click.option("-o", "--output", default="outputs", help="Path to the output folder")
@click.option("-g", "--genre", help="Filter by a desired genre", required=True)
@click.option("-y", "--year", help="Filter by a desired minimum year", required=True)

# Main function
def main(input, output, genre, year):
    """
    Main function to import a dataset and perform filtering
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

    # Create the output folder if it doesn't exist
    if not os.path.exists(output):
        os.makedirs(output)

    # Create FilteringClass instance
    filtering_instance = FilteringClass(df)

    # Debugging point
    import pdb; pdb.set_trace()

    # Filter by genre and year
    filtered_df_genre = filtering_instance.filter_by_genre(genre)
    filtered_df_year = filtering_instance.filter_by_year(year)

    # Combine filters
    filtered_df = pd.concat([filtered_df_genre, filtered_df_year], axis=0).drop_duplicates()

    # Save the filtered DataFrame as "filtered_output.csv" in the output folder
    output_filtered_file_path = os.path.join(output, "filtered_output.csv")
    filtered_df.to_csv(output_filtered_file_path, index=False)

    print(f"Original DataFrame Shape: {df.shape}")
    print(f"Filtered DataFrame Shape: {filtered_df.shape}")
    print(f"Filtered data saved to: {output_filtered_file_path}")

if __name__ == "__main__":
    print("The code is properly working!")
    main()
    
   # python scripts/filmgenre_script.py -i datasets/FilmGenreStats.csv -g "Genre" -y "Year"

    # Genres --> Adventure, Action, Drama, Comedy, Thriller or Suspense, Horror, Romantic Comedy, 
    #           Musical, Documentar, Dark Comedy, Western, Concert or Performance, Multiple Genres, Reality

    # Year --> ranging 1995 / 2017