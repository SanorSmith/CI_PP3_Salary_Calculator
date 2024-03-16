from config import SHEET
from main import ask_restart_or_exit, main
import ui_helpers as ui_h
import re


def validate_email(email):
    """
    Validates an email address to ensure it follows the user_email@domain.com format.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_regex, email) is not None


def ask_the_user(prompt):
    """
    Asks the user a yes/no question based on the provided prompt.

    Args:
        prompt (str): The message to display to the user.

    Returns:
        bool: True if the user answers 'yes', False if 'no'.
    """
    response_map = {'yes': True, 'y': True, 'no': False, 'n': False}
    
    while True:
        response = input(prompt).lower().strip()
        if response in response_map:
            return response_map[response]
        else:
            print("Invalid input. Please enter (yes/no): ")

            
def register_user():
    """
    Registers a new user by asking for their name and email, then pushes the data to the 'reg_user_list' worksheet.
    """
    name = input("Enter your name: ")
    while True:
        email = input("Enter your email address for registration: ")
        if validate_email(email):
            break
        else:
            print("\033[31m" + "Invalid email format. Please try again." + "\033[0m")  
    if is_email_registered(email):
        print("\033[33m" + "You are already registered." + "\033[0m")
        response = ask_the_user("Would you like to proceed using the registered email? (yes/no): ")
        if response : return
        else : 
            if not ask_restart_or_exit():
                exit()
                ui_h.print_with_delay("Thank you for using the application!")
            else:
                main() 
    try:
        worksheet = SHEET.worksheet('reg_user_list')
        worksheet.append_row([name, email])
        print("\033[32m" + "Registration successful." + "\033[0m")
        response = ask_the_user("Do you want to preceed to Salary Calculator? (yes/no): ")
        if response : return
        else : 
            if not ask_restart_or_exit():
                exit()
                ui_h.print_with_delay("Thank you for using the application!")
            else:
                main()
    except Exception as e:
        print(f"An error occurred while registering: {e}")


def check_returning_user():
    """
    Checks if a returning user's email is in the worksheet and displays a welcome message.
    """
    while True:
        email = input("Enter your email address to continue: ")
        if validate_email(email):
            break
        else:
            print("\033[31m" +"Invalid email format. Please try again." + "\033[0m")
    
    try:
        worksheet = SHEET.worksheet('reg_user_list')
        user_data = worksheet.get_all_values()
        
        for row in user_data:
            if email == row[1]:  # row[1] is the email column
                print(f"Welcome back, {row[0]}!")  # row[0] is the name column
                return True  # Email found, user is registered

        print("\033[33m" + "Email not found." + "\033[0m")
        return False  # Email not found, user is not registered
    except Exception as e:
        print(f"An error occurred while checking user: {e}")


def is_email_registered(email):
    """
    Checks if the given email is already registered.

    :param email: The email address to check.
    :return: True if the email is registered, False otherwise.
    """
    try:
        worksheet = SHEET.worksheet('reg_user_list')
        emails = worksheet.col_values(2)
        return email in emails
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    