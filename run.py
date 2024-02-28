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

def validate_job_choice(choice, max_choice):
    """
    Validate the user's job choice input.
    """
    if not choice.isdigit():
        raise ValueError("Input must be a number.")
    
    choice = int(choice)
    if not 1 <= choice <= max_choice:
        raise ValueError(f"Input must be a number between 1 and {max_choice}.")
    
    return choice


def validate_choice(choice, max_choice):
    """
    Validate the user's choice input.
    """
    if not choice.isdigit():
        raise ValueError("Input must be a number.")
    
    choice = int(choice)
    if not 1 <= choice <= max_choice:
        raise ValueError(f"Input must be a number between 1 and {max_choice}.")
    
    return choice


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
    for row in data[0:]:  # Skip the header row if there is one
        total_salary += sum(int(value) for value in row[1:] if value.isdigit())

    return total_salary

def calculate_vat_and_salary(total_salary):
    """
    Function to calculate VAT and remaining salary based on the user's job selection.
    """
    try:
        vat_job_worksheet = SHEET.worksheet('vat_job_list')        
        job_vat_data = vat_job_worksheet.get_all_values()

        print("Job List:")
        for index, (job, vat_rate) in enumerate(job_vat_data, start=1):
            print(f"{index}. {job}")
            
            
        # Get user's job choice
        while True:
            try:
                job_choice_input = input("Select your job by entering the corresponding number: ")
                job_choice = validate_job_choice(job_choice_input, len(job_vat_data))
                break
            except ValueError as e:
                print(f"Input error: {e}")

        selected_job, selected_vat_rate = job_vat_data[job_choice - 1]
        # Calculate VAT and remaining salary
        vat_rate = float(selected_vat_rate)
        vat_amount = total_salary * (vat_rate)
        remaining_salary = total_salary - vat_amount

        # Display results
        #print(f"Selected Job: {selected_job}")
        #print(f"VAT Rate: {vat_rate}%")
        #print(f"VAT Amount: {vat_amount}")
        #print(f"Remaining Salary: {remaining_salary}")
        
        return remaining_salary, selected_job, vat_rate, vat_amount
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
        

def calculate_net_salary(remaining_salary):
    """
    Function to calculate and display net salary after tax deduction based on the user's county selection.
    """
    try:
        # Access the worksheet
        counties_worksheet = SHEET.worksheet('counties_tax_rate')
        # Get all counties names and tax rates
        counties_data = counties_worksheet.get_all_values()

        # Display counties to the user
        print("Counties List:")
        for index, (county, _) in enumerate(counties_data, start=1):
            print(f"{index}. {county}")

        # Get and validate user's county choice
        while True:
            try:
                county_choice_input = input("Select your county by entering the corresponding number: ")
                county_choice = validate_choice(county_choice_input, len(counties_data))
                break
            except ValueError as e:
                print(f"Input error: {e}")

        selected_county, selected_tax_rate = counties_data[county_choice - 1]

        # Calculate tax and net salary
        tax_rate = float(selected_tax_rate.replace(',','.'))
        tax_amount = remaining_salary * (tax_rate / 100)
        net_salary = remaining_salary - tax_amount

        # Display results
        #print(f"Selected County: {selected_county}")
        #print(f"Tax Rate: {tax_rate}%")
        #print(f"Tax Amount: {tax_amount}")
        #print(f"Net Salary: {net_salary}")
        
        return selected_county, tax_rate, tax_amount, net_salary

    except Exception as e:
        print(f"An error occurred: {e}")
        
        
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
    

def welcome_message():
    """
    Function to display a welcome message to the user.
    """
    print("Welcome to the Salary Calculator program.")

    print("This application assists individuals in computing their monthly net income by utilizing mathematical formulas and tax data. It simplifies the process of calculating monthly salaries and provides accurate tax amounts based on county tax tables.")

    print ("Let's get started!")
    print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////// \n")
    
 
def processing_data_input_output():
    """
    Function to process user input and calculate output 
    """
    name, salary_data = get_user_input()
    total_salary = sum(salary_data)
    push_data_to_spreadsheet(name, salary_data)
    job_name, vat_rate, vat_amount, remaining_salary = calculate_vat_and_salary(total_salary)
    county_name, tax_rate, tax_amount, net_salary = calculate_net_salary(remaining_salary) 
    output_details = [
        ("User Name", name),
        ("Entered Salaries", salary_data),
        ("Total Salary", total_salary),
        ("Chosen Job Name", job_name),
        ("VAT Rate", f"{vat_rate}%"),
        ("Salary After VAT Reduction", remaining_salary),
        ("Selected County Name", county_name),
        ("Tax Rate for Selected County", f"{tax_rate}%"),
        ("Tax Amount", tax_amount),
        ("Net Salary", net_salary)
    ]

    # Print the final summary in a table format
    print("\nFinal Summary:")
    print(f"{'Detail':<30} | {'Value'}")
    print("-" * 50)
    for detail in output_details:
        print(f"{detail[0]:<30} | {detail[1]}")   
    
    
def main(): 
    """
    Program main function
    """
    welcome_message()
    processing_data_input_output()    
    reset_spreadsheet()
    
main()