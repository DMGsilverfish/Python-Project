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

        return amount, year, month, day, region_name
    except ValueError:
        print("Invalid input format. Please enter the date in the format YYYY-MM-DD.")
        return get_sales_data()

def calculate_quarter(month: int) -> int:

    """Calculate the quarter based on the month."""

    if 1 <= month <= 3:

        return 1

    elif 4 <= month <= 6:

        return 2

    elif 7 <= month <= 9:

        return 3

    else:

        return 4