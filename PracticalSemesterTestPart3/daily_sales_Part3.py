# daily_sales.py

class DailySales:
    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, amount, date, region, quarter):
        self.amount = amount
        self.date = date
        self.region = region
        self.quarter = quarter

    @classmethod
    def from_csv_row(cls, csv_row):
        # Implement logic to create a DailySales object from a CSV row
        pass

    def to_csv_row(self):
        # Implement logic to convert a DailySales object to a CSV row
        pass

    def is_valid(self):
        # Implement data validation logic here
        pass
