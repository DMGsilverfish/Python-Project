from typing import List, Tuple 

def get_sales_data() -> Tuple[float, int, int, int]:

    """Get sales data from the user."""

    try:

        amount = float(input("Enter sales amount: "))

        year = int(input("Enter year: "))

        month = int(input("Enter month: "))

        day = int(input("Enter day: "))

        return amount, year, month, day

    except ValueError:

        print("Invalid input. Please enter valid numeric values.")

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