from sales_processor import salesDataProcessor, FileImportError

def main():
    sales_processor = salesDataProcessor()

    while True:
        print("SALES DATA IMPORTER")
        print("")
        print("COMMAND MENU\n")
        print("view\t- View all sales")
        print("add\t- Add sales")
        print("import\t- Import sales from file")
        print("menu\t- Show menu")
        print("exit\t- Exit Program")

        choice = input("Please enter a command: ")

        if choice == "view":
            sales_processor.display_sales_data()
        elif choice == "add":
            new_sale = sales_processor.get_sales_data_from_user()
            sales_processor.sales_list.add_sales_data(new_sale)
        elif choice == "import":
            filename = input("Enter the CSV file name to import: ")
            try:
                sales_processor.import_sales_data_from_file(filename)
            except FileImportError as e:
                print(e)
        elif choice == "menu":
            print("COMMAND MENU\n")
            print("view\t- View all sales")
            print("add\t- Add sales")
            print("import\t- Import sales from file")
            print("menu\t- Show menu")
            print("exit\t- Exit Program")
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
