import csv
from tabulate import tabulate

def csv_table(csv_filepath):
    """
    Reads a CSV file and prints its content in a formatted table.
    """
    try:
        with open(csv_filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Read the header row
            data = list(reader)     # Read the remaining data rows

            print(tabulate(data, headers=headers, tablefmt="grid"))
            # You can change 'grid' to other formats like 'simple', 'plain', 'fancy_grid', 'pipe', 'orgtbl', etc.
    except FileNotFoundError:
        print(f"Error: The file '{csv_filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

from fpath import fp, fp2

print('\n\n\nData :\n')
csv_table(fp)
print('\n\nRelative Efficiency Data :\n')
csv_table(fp2)
print('\n\n\n')