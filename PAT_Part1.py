from PAT_Part1_Sales import get_sales_data, calculate_quarter
from PAT_Part1_File_Operation import read_sales_data, write_sales_data

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

def main():
    csv_filename = "PythonPAT_CSV"
    imported_files = set()

    # Read existing sales data from CSV file
    sales_data = read_sales_data(csv_filename)

    while True:
        print("\nCOMMAND MENU:")
        print("view   - View all sales")
        print("add    - Add sales")
        print("import - Import sales from file")
        print("menu   - Show menu")
        print("exit   - Exit program")

        choice = input("\nPlease enter a command: ").lower()
        total = 0

        if choice == 'view':
             # Define headers and calculate the maximum width for each column
            headers = ["Date", "Quarter", "Amount"]
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
            for entry in sales_data:
                date = f"{entry[1]}-{entry[2]}-{entry[3]}"
                row = [date, entry[4], str(entry[0])]
                total += float(entry[0])
                print(" | ".join(row[i].ljust(max_widths[i]) for i in range(len(row))))
            print(separator)    
            print("\t  | TOTAL:   " + str(total) + "\n")
        elif choice == 'add':
            # Add new sales data
            sales_entry = get_sales_data()
            amount, year, month, day = sales_entry
            if validate_sales_data(amount, year, month, day):
                quarter = calculate_quarter(month)
                sales_data.append([str(amount), str(year), str(month), str(day), str(quarter)])
                print("\nSales for " + str(year)+"-" + str(month) + "-" + str(day) + " added.")
                
            else:
                print("Invalid sales data. Please check your inputs.")
        elif choice == 'import':
            # Import sales data from CSV
            filename = input("Enter the name of the CSV file to import: ")
            if filename not in imported_files:
                imported_files.add(filename)
                imported_data = read_sales_data(filename)
                # Validate and append imported data to sales_data
                # Handle invalid data using asterisks and question marks as needed
                pass
            else:
                print("This file has already been imported.")
        elif choice == 'menu':
            # Save and quit
            write_sales_data(csv_filename, sales_data)
            pass
        elif choice == 'exit':
            exit()
        else:
            print("Invalid choice")    

if __name__ == "__main__":
    main()
