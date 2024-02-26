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


def get_user_input():
    """
    Function to get user input for name, number of days, and daily salary.
    """
   
    name = input("Enter your name: ")
           
    days = int(input("Enter the number of days (up to 31): "))
           
    salary_data = []
    for day in range(1, days + 1):                
                salary = int(input(f"Enter salary for day {day}: "))
                salary_data.append(salary)               

    return name, salary_data

#Call 
name, salary_data = get_user_input()