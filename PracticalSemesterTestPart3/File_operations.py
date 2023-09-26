import csv

def save_sales_data_to_csv(filename, sales_list):
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for sale in sales_list:
            csv_writer.writerow(sale.to_list())

def read_sales_data_from_csv(filename):
    with open(filename, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row[filename])

if __name__ == "__main__":
    pass
