# sales_list.py

class SalesList:
    def __init__(self):
        self.sales_data = []

    def add_sales(self, daily_sales):
        self.sales_data.append(daily_sales)

    def get_sales_by_index(self, index):
        if 0 <= index < len(self.sales_data):
            return self.sales_data[index]
        return None

    def import_sales_data(self, filename):
        # Implement logic to import sales data from a file
        pass

    def __len__(self):
        return len(self.sales_data)

    def __iter__(self):
        return iter(self.sales_data)
