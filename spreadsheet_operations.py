from config import SHEET
from ui_helpers import print_user_data_table, print_with_delay
def push_data_to_spreadsheet(name, salary_data):
    """
    Function to push data to the spreadsheet using append_row.
    """
    try:
        print ("\nupdating salary worksheet...\n")
        worksheet = SHEET.worksheet('operation_table')
        salary_data_int = [int(salary) for salary in salary_data]
        new_row = [name] + salary_data_int
        worksheet.append_row(new_row)
        print("Salary worksheet updated successfully. \n")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def sum_salary_from_spreadsheet():
    """
    Function to sum up salary data from the spreadsheet.
    """
    
    worksheet = SHEET.worksheet('operation_table')
    data = worksheet.get_all_values()

    total_salary = 0
    for row in data[0:]:  # Skip the header row if there is one
        total_salary += sum(int(value) for value in row[1:] if value.isdigit())

    return total_salary

def push_all_u_c_data(output_details):
    """
    Pushes data from output_details to the 'all_users_calculated_data' worksheet.
    :param output_details: Tuple of tuples containing the data to be pushed.
    """
    try:
        worksheet = SHEET.worksheet('all_users_calculated_data')
        headers = [label for label, _ in output_details]
        values = [str(value) for _, value in output_details]
        if worksheet.row_count == 0 or not worksheet.row_values(1):
            worksheet.append_row(headers)
        worksheet.append_row(values)

    except Exception as e:
        print(f"An error occurred while updating the spreadsheet: {e}")

def reset_spreadsheet(worksheet_name):
    """
    Function to reset the spreadsheet by clearing all its contents.
    """
    
    worksheet = SHEET.worksheet(worksheet_name)        
    worksheet.clear()
    print("Spreadsheet has been reset.")
    
def print_all_user_calculated_data():
    """
    Reads and prints all data from the 'all_users_calculated_data' worksheet in a formatted table.
    """
    try:
        worksheet = SHEET.worksheet('all_users_calculated_data')
        data = worksheet.get_all_values()

        if not data:
            print_with_delay("No data found in the worksheet.")
            return

        # Convert each row to a list of tuples
        for row in data[1:]:  # Skipping header row
            output_details = list(zip(data[0], row))  # Zipping headers with row values
            print_user_data_table(output_details)

    except Exception as e:
        print_with_delay(f"An error occurred while retrieving data from the spreadsheet: {e}")