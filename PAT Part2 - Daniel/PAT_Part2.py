#s224082124, Daniel Gibson
from PAT_Part2_Sales import get_sales_data, check_sales_data, calculate_quarter
from PAT_Part2_File_Operation import read_sales_data, write_sales_data
import re
import csv

def is_valid_filename(filename):
    # Define a regular expression pattern to match the desired format
    pattern = r'^sales_q[1-4]_\d{4}_[mcew]\.csv$'
    return re.match(pattern, filename)

def validate_sales_data(amount: float, year: int, month: int, day: int) -> bool:
    """Validate sales data."""
    if amount <= 0 or year < 2000 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    if month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False
    if month == 2 and (day < 1 or day > 28):
        return False
    if day < 1 or day > 31:
        return False
    return True

def display(sales_data):
    # Define headers and calculate the maximum width for each column
    headers = ["        Date", " Quarter", "Region", "Amount"]
    max_widths = [len(header) for header in headers]

    # Calculate the maximum width for each column based on data
    for entry in sales_data:
        max_widths[0] = max(max_widths[0], len(f"{entry[1]}-{entry[2]}-{entry[3]}"))
        max_widths[1] = max(max_widths[1], len(entry[4]))
        max_widths[2] = max(max_widths[2], len(str(entry[0])))

    # Create a horizontal line separator
    separator = "=" * (sum(max_widths) + len(max_widths) * 3 + 1)

    # Print headers
    print(" | ".join(header.ljust(max_widths[i]) for i, header in enumerate(headers)))
    print(separator)

    # Print data
    num = 0
    total = 0
    for entry in sales_data:
        num += 1
        date = f"{entry[1]}-{entry[2]}-{entry[3]}"
        if entry[4] == 'Mountain':
            row = [str(num) + ". ", date, " " + str(entry[5]) + " ", entry[4], str(entry[0])]
        else:
            row = [str(num) + ". ", date, " " + str(entry[5]) + " ", entry[4] + "\t", str(entry[0])] 
        total += float(entry[0])

        max_widths = [len(str(num) + ". ")]
        max_widths.extend(len(item) for item in row[1:])

        print(" | ".join(row[i].ljust(max_widths[i]) for i in range(len(row))))

    amount_width = max_widths[-1]

    print(separator)
    print("TOTAL:".ljust(max_widths[0] + max_widths[1] + max_widths[2]), end="   ")
    print(" " * 17 + "{:.2f}".format(total))
    print(separator)

def main():
    csv_filename = "sales_q2_2020_m.csv"
    imported_files = set()

    # Read existing sales data from CSV file
    sales_data = read_sales_data(csv_filename)

    print("SALES DATA IMPORTER")

    while True:
        print("\nCOMMAND MENU:")
        print("view     - View all sales")
        print("add      - Add sales")
        print("import   - Import sales from file")
        print("menu     - Show menu")
        print("exit     - Exit program")

        choice = input("\nPlease enter a command: ").lower()
        total = 0

        if choice == 'view':
             display(sales_data)
        elif choice == 'add':
             # Add new sales data
             sales_entry = get_sales_data()
             amount, year, month, day, quarter,  region_name = sales_entry
             if validate_sales_data(amount, year, month, day):
                sales_data.append([amount, year, month, day, region_name, quarter])
                print("\nSales for {}-{}-{} added.".format(year, month, day))
             else:
                print("Invalid sales data. Please check your inputs.")

        elif choice == 'import':
        # Import sales data from CSV
            filename = input("Enter the name of the CSV file to import: ")
            importDataFile = "PAT_Part2_ImportData.csv"
            with open(importDataFile, 'w', newline='') as csvFile:
                pass

            if filename.endswith(".csv") and filename[-5] in ['w', 'm', 'c', 'e']:
                if is_valid_filename(filename):
                    if filename not in imported_files:
                        imported_files.add(filename)
                        imported_data = read_sales_data(filename)
                        print(f"File '{filename}' has been successfully imported.")
                        print("\nImported data:")
                        is_valid = True
                        valid_data = []  # Create a list to store valid data

                        for data_entry in imported_data:
                            if not check_sales_data(data_entry):
                                is_valid = False
                                print("Bad data was found in the file and replaced with a '?'")  # Print "Bad data" for invalid entries

                        
                        with open(importDataFile, mode='r') as csv_file:
                            csv_reader = csv.reader(csv_file)
                            for row in csv_reader:
                                valid_data.append(row)

                        # Display all valid data
                        display(valid_data)
                        if is_valid == False:
                            print("Select a file with good data please!")  # Print "Bad data" for invalid entries

                    else:
                        print("This file has already been imported.")
                else:
                    print("Invalid filename format. Please use sales_qn_yyyy_r.csv format.")
            else:
                print(f"File name '{filename}' doesn't include one of the following region codes: ['w', 'm', 'c', 'e'].")
  

        elif choice == 'menu':
            # Save and quit
            write_sales_data(csv_filename, sales_data)
            pass
        elif choice == 'exit':
            print("\nBye!")
            exit()
        else:
            print("Invalid choice")    

if __name__ == "__main__":
    main()