import gspread
from google.oauth2.service_account import Credentials 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('salary_calculater')

                                                                                                                                                                                 

#Validate User input data function 
def validate_name(name):
    """
    Validate the provided name. The name should be non-empty and contain only letters.
    """
    if not name.strip():
        raise ValueError("The name cannot be empty.")
    if not name.replace(' ', '').isalpha():  # Allowing spaces in names
        raise ValueError("The name must contain only letters.")
    return name.strip()

def validate_days(days):
    """
    Validate the number of days.
    """
    if not 1 <= days <= 31:
        raise ValueError("The number of days must be between 1 and 31.")
    return days

def validate_salary(salary):
    """
    Validate the salary amount.
    """
    if salary < 0:
        raise ValueError("Salary cannot be negative.")
    return salary

def get_user_input():
    """
    Function to get user input for name, number of days, and daily salary.
    """
    while True:
            try:
                name = validate_name(input("Enter your name: "))
                break
            except ValueError as e:
                print(f"Input error: {e}")
           
    while True:
        try:
            days = validate_days(int(input("Enter the number of days (up to 31): ")))
            break
        except ValueError as e:
            print(f"Input error: {e}")
           
    salary_data = []
    for day in range(1, days + 1):
        while True:
            try:
                
                salary = validate_salary(int(input(f"Enter salary for day {day}: ")))
                
                salary_data.append(salary)
                
                break
            except ValueError as e:
                print(f"Input error: {e}")               

    return name, salary_data


def push_data_to_spreadsheet(name, salary_data):
    """
    Function to push data to the spreadsheet using append_row.
    """
    try:
        print ("updating salary worksheet...\n")
        worksheet = SHEET.worksheet('total_paid_lifts')
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
    
    worksheet = SHEET.worksheet('total_paid_lifts')
    data = worksheet.get_all_values()

    total_salary = 0
    for row in data[1:]:  # Skip the header row if there is one
        total_salary += sum(int(value) for value in row[1:] if value.isdigit())

    return total_salary
        
def print_result():
    """
    Function to print out the result.
    """
    try:
        worksheet = SHEET.worksheet('total_paid_lifts')
        data = worksheet.get_all_values()
        print("Data in 'total_paid_lifts':")
        for row in data:
            print(row)
    except Exception as e:
        print(f"An error occurred: {e}")  

def reset_spreadsheet():
    """
    Function to reset the spreadsheet by clearing all its contents.
    """
    
    worksheet = SHEET.worksheet('total_paid_lifts')        
    worksheet.clear()
    print("Spreadsheet has been reset.")
    
 


def main(): 
    """
    Program main function
    """
    name, salary_data = get_user_input()
    push_data_to_spreadsheet(name, salary_data)
    print_result()
    total_salary = sum_salary_from_spreadsheet()
    print(f"Total Salary: {total_salary}")
    #reset_spreadsheet()
    
main()