import csv
from typing import List

def read_sales_data(filename: str) -> List[List[str]]:
    """Read sales data from a CSV file."""
    sales_data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                sales_data.append(row)
    except FileNotFoundError:
        print("CSV file not found.")
    return sales_data

def write_sales_data(filename: str, data: List[List[str]]) -> None:
    """Write sales data to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

