from config import SHEET
from main import ask_restart_or_exit, main
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
            print("Invalid input. Please enter 'yes' or 'no'.")

            
def register_user():
    """
    Registers a new user by asking for their name and email, then pushes the data to the 'reg_user_list' worksheet.
    """
    name = input("Enter your name: ")
    email = input("Enter your email address for registration: ")
    if is_email_registered(email):
        print("You are already registered.")
        response = ask_the_user("Would you like to proceed using the registered email? Please respond with 'yes' or 'no'.")
        if response : return
        else : 
            if not ask_restart_or_exit():
                exit()
                print("Thank you for using the application!")
            else:
                main() 
    try:
        worksheet = SHEET.worksheet('reg_user_list')
        worksheet.append_row([name, email])
        print("Registration successful.")
    except Exception as e:
        print(f"An error occurred while registering: {e}")

def check_returning_user():
    """
    Checks if a returning user's email is in the worksheet and displays a welcome message.
    """
    email = input("Enter your email address to continue: ")
    
    try:
        worksheet = SHEET.worksheet('reg_user_list')
        emails = worksheet.col_values(2)
        name = worksheet.col_values(1)
        if email in emails:
            print(f"Welcome back, {name}!")
            return email
        else:
            print("Email not found.")
            response = ask_the_user("Would you like to register? (yes/no): ")
            if response :
                return True
            else:
                print("Registration skipped.")
                return False
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
        emails = worksheet.col_values(2)  # Assuming email is in the second column
        return email in emails
    except Exception as e:
        print(f"An error occurred: {e}")
        return False