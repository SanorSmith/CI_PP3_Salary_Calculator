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
                salary = int(input(f"Enter salary for day {day}: "))
                salary_data.append(salary)               

    return name, salary_data

#Call 
name, salary_data = get_user_input()