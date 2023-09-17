import csv
from typing import List, Tuple

# Define the region dictionary
regions = {
    'm': 'Mountain',
    'c': 'Central',
    'e': 'East',
    'w': 'West'
}

def get_sales_data() -> Tuple[float, int, int, int, str]:
    """Get sales data from the user."""
    try:
        date_input = input("Enter date (YYYY-MM-DD): ")
        year, month, day = map(int, date_input.split('-'))

        amount = float(input("Enter sales amount: "))

        region_code = input("Enter region code (m, c, e, w): ").lower()
        region_name = regions.get(region_code, 'Unknown')

        q = calculate_quarter(month)

        return amount, year, month, day, q,  region_name
    except ValueError:
        print("Invalid input format. Please enter the date in the format YYYY-MM-DD.")
        return get_sales_data()

def calculate_quarter(month: int) -> int:
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    else:
        return 4
    
def check_sales_data(data: List[str]) -> bool:
    # Check if there are enough elements in the data list
    if len(data) != 6:
        print("?")
        return False

    amount, year, month, day, region, quarter = data

    # Initialize a list to store modified data for writing to the CSV file
    modified_data = list(data)

    # Check if the price is in the correct format (a positive float)
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError()
    except ValueError:
        modified_data[0] = "?"  # Replace bad data with "?"

    # Validate the year, month, and day separately
    try:
        year = int(year)
        if year < 2000 or year > 9999:
            raise ValueError()
    except ValueError:
        modified_data[1] = "?"  # Replace bad year with "?"

    try:
        month = int(month)
        if month < 1 or month > 12:
            raise ValueError()
    except ValueError:
        modified_data[2] = "?"  # Replace bad month with "?"

    try:
        day = int(day)
        if day < 1 or day > 31:
            raise ValueError()
        if (month in [4, 6, 9, 11] and day > 30) or (month == 2 and day > 28):
            raise ValueError()
    except ValueError:
        modified_data[3] = "?"  # Replace bad day with "?"

    # Check if the region is in the specified range
    if region not in ['Mountain', 'Central', 'East', 'West']:
        modified_data[4] = "?"  # Replace bad data with "?"

    # Check if the quarter is in the range of 1 to 4
    try:
        quarter = int(quarter)
        if quarter < 1 or quarter > 4:
            raise ValueError()
    except ValueError:
        modified_data[5] = "?"  # Replace bad data with "?"

    # Write the modified data (whether valid or invalid) to the CSV file
    with open("PAT_Part2_ImportData.csv", mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(modified_data)

    # Check if any data is marked as invalid ("?"), and return False if found
    if any(value == "?" for value in modified_data):
        return False
    else:
        # Return True if all checks pass (no "?" found in the modified data)
        return True
