from validation import validate_input
import spreadsheet_operations as sp_ops
from ui_helpers import clear_screen, print_centered_box, welcome_message, print_user_data_table

def get_user_type():
    """
    Asks the user if they are a single individual or a company with multiple employees.
    Returns 'company' if the user is a company, 'individual' otherwise.
    """
    while True:
        print("Are you a single individual or a company with multiple employees?\n")
        user_type_input = input("(Enter (1) Individual  or  (2) Company): ").lower().strip()
        if user_type_input in ['1', '2']:
            return user_type_input
        else:
            print("Invalid input. Please enter 'individual' or 'company'.")
            

def get_user_input(user_type, emp_num=None):
    """
    Function to get user input for name, number of days, and daily salary.
    """
    if user_type =='1':
        name_prompt = "Enter your/employee's name please: "
    else:
        name_prompt = f"Enter employee's no.{emp_num+1} name please: "
    while True:
            try:
                name = validate_input(input(name_prompt), "name")
                break
            except ValueError as e:
                print(f"Input error: {e}")
           
    while True:
        try:
            days = validate_input(input("Enter the number of days to calculate (up to 31 days): "), "days")
            break
        except ValueError as e:
            print(f"Input error: {e}")
           
    salary_data = []
    for day in range(1, days + 1):
        while True:
            try:
                
                salary = validate_input(input(f"Enter salary for day {day}: "), "salary")
                
                salary_data.append(salary)
                
                break
            except ValueError as e:
                print(f"Input error: {e}")               

    return name, salary_data
        
def get_number_of_employees():
    """
    Asks the user for the number of people who will be entering their salary details.
    Returns an integer representing this number.
    """
    while True:
        try:
            num_employees = int(input("\nEnter the number of people who will be entering their salary details: "))
            if num_employees > 0:
                return num_employees
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def calculate_vat_and_salary(total_salary):
    """
    Function to calculate VAT and remaining salary based on the user's job selection.
    """
    try:
        vat_job_worksheet = sp_ops.SHEET.worksheet('vat_job_list')        
        job_vat_data = vat_job_worksheet.get_all_values()        
        print("Categories of Occupations:")
        for index, (job, vat_rate) in enumerate(job_vat_data, start=1):
            print(f"{index}. {job}")
            
            
        # Get user's job choice
        while True:
            try:
                print("")
                job_choice_input = input("Choose your category's occupations by entering the corresponding number: ")
                job_choice = validate_input(job_choice_input,"choice", len(job_vat_data))
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
        counties_worksheet = sp_ops.SHEET.worksheet('counties_tax_rate')
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
                county_choice = validate_input(county_choice_input,"choice" ,len(counties_data))
                break
            except ValueError as e:
                print(f"Input error: {e}")

        selected_county, selected_tax_rate = counties_data[county_choice - 1]

        # Calculate tax and net salary
        tax_rate = float(selected_tax_rate.replace(',','.'))
        tax_amount = remaining_salary * (tax_rate / 100)
        net_salary = remaining_salary - tax_amount
        clear_screen()
        # Display results
        #print(f"Selected County: {selected_county}")
        #print(f"Tax Rate: {tax_rate}%")
        #print(f"Tax Amount: {tax_amount}")
        #print(f"Net Salary: {net_salary}")
        
        return selected_county, tax_rate, tax_amount, net_salary

    except Exception as e:
        print(f"An error occurred: {e}")

def processing_data_input_output(user_type, emp_num=None):
    """
    Function to process user input and calculate output 
    """
    name, salary_data = get_user_input(user_type, emp_num)
    total_salary = sum(salary_data)
    sp_ops.push_data_to_spreadsheet(name, salary_data)
    remaining_salary, job_name, vat_amount, vat_rate = calculate_vat_and_salary(total_salary)
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
    sp_ops.pull_all_u_c_data(output_details)
    if ask_print_results():
        print_user_data_table(output_details)

    return name

def ask_print_results():
    """
    Asks the user if they want to print the calculation results.
    Returns True if the user wants to print, False otherwise.
    """
    while True:
        try:
            choice = input("Do you want to print the calculation results? (yes/no): ")
            validated_choice = validate_input(choice, "choice_c_r")
            if validated_choice in ['yes', 'y']:
                return True
            elif validated_choice in ['no', 'n']:
                return False
        except ValueError as e:
            print(f"Input error: {e}")

