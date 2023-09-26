from decimal import Decimal
from datetime import datetime
import csv

DATE_FORMAT = '%Y%m-%d'

class Region:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __str__(self):
        return f"{self.code} - {self.name}"

class Regions:
    def __init__(self):
        self.valid_regions = [
            Region('w', 'West'),
            Region('m', 'Mountain'),
            Region('c', 'Central'),
            Region('e', 'East')
        ]

    def get_region_by_code(self, code):
        for region in self.valid_regions:
            if region.code == code:
                return region
        return None

    def get_valid_region_codes(self):
        return [region.code for region in self.valid_regions]

    def __str__(self):
        return ", ".join([str(region) for region in self.valid_regions])

class DailySales:
    def __init__(self, amount, date, region):
        self.amount = amount
        self.date = date
        self.region = region
        self.quarter = self.calculate_quarter()

    def calculate_quarter(self):
        return (self.date.month - 1) // 3 + 1

    def to_list(self):
        return [
            float(self.amount),
            self.date.strftime(DATE_FORMAT),
            self.quarter,
            self.region.code
        ]

    @classmethod
    def from_csv_row(cls, csv_row, regions):
        try:
            amount = Decimal(csv_row[0])
            date_str = csv_row[1]
            date = datetime.strptime(date_str, DATE_FORMAT)

            region_code = csv_row[3].lower()
            if region_code not in regions.get_valid_region_codes():
                raise ValueError("Invalid region code.")

            return cls(amount, date, regions.get_region_by_code(region_code))
        except (ValueError, IndexError, KeyError):
            return None

    def is_valid(self):
        return (
            self.amount > Decimal('0') and
            1 <= self.date.month <= 12 and
            1 <= self.date.day <= 31 and
            (self.date.month != 2 or self.date.day <= 28) and
            (self.date.month in [4, 6, 9, 11] or self.date.day <= 30) and
            2000 <= self.date.year <= 9999
        )

class SalesList:
    def __init__(self):
        self.sales_data = []
        self.bad_data = False

    def __iter__(self):
        return iter(self.sales_data)

    def __len__(self):
        return len(self.sales_data)

    def add_sales_data(self, data):
        if data.is_valid():
            self.sales_data.append(data)
        else:
            self.bad_data = True

    def get_sales_data_by_index(self, index):
        if 0 <= index < len(self.sales_data):
            return self.sales_data[index]
        return None

    def add_sales_list(self, other_list):
        if isinstance(other_list, SalesList):
            self.sales_data.extend(other_list.sales_data)
            if other_list.bad_data:
                self.bad_data = True

class salesDataProcessor:
    def __init__(self):
        self.sales_list = SalesList()
        self.regions = Regions()
        self.imported_files = set()

    def get_valid_date(self):
        while True:
            date_str = input("Enter a valid date (YYYY-MM-DD): ")
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d')
                return date
            except ValueError:
                print("Invalid date format. Please enter a valid date in YYYY-MM-DD.")

    def get_sales_data_from_user(self):
        try:
            amount = Decimal(input("Amount: "))
            date = self.get_valid_date()

            if amount <= Decimal('0'):
                raise ValueError("Invalid input. Please check your sales data.")

            region = self.get_valid_region()

            return DailySales(amount, date, region)
        except ValueError:
            print("Invalid input. Please enter valid numeric values and a valid region code.")

    def get_valid_region(self):
        while True:
            region_code = input(f"Enter sales region code ({self.regions}): ").lower()
            if region_code in self.regions.get_valid_region_codes():
                return self.regions.get_region_by_code(region_code)
            else:
                print("Invalid region code. Please enter a valid region code.")

    def import_sales_data_from_file(self, filename):
        try:
            if filename in self.imported_files:
                raise FileImportError(f"The file '{filename}' has already been imported.")

            with open(filename, 'r') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    sales_data = DailySales.from_csv_row(row, self.regions)
                    if sales_data and sales_data.is_valid():
                        self.sales_list.add_sales_data(sales_data)
                    else:
                        print(f"Bad imported data in file '{filename}': {row}")

                self.imported_files.add(filename)

        except (ValueError, FileNotFoundError) as e:
            raise FileImportError(f"File not found or invalid file: {filename}")

        except FileImportError as e:
            print(e)

    def display_sales_data(self):
        for sale in self.sales_list:
            record = sale.to_dict()
            region_name = sale.region.name
            print("\tDate\t\tQuarter\t\tRegion\t\tAmount\n-----------------------------------------")
            print(f"{record['date']}\t{record['quarter']}\t{region_name}\t{record['amount']}")

class FileImportError(OSError):
    pass

if __name__ == "__main__":
    pass
