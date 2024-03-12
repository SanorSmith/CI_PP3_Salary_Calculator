from config import SHEET

def ask_if_new_user():
    """
    Asks the user if they have used the app before.

    Returns:
        bool: True if the user is new, False otherwise.
    """
    while True:
        response = input("Have you used Salary Calculator before? (yes/no): ").lower().strip()
        if response in ['yes', 'y']:
            return False
        elif response in ['no', 'n']:
            return True
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            
def register_user():
    """
    Registers a new user by asking for their name and email, then pushes the data to the 'reg_user_list' worksheet.
    """
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    
    try:
        worksheet = SHEET.worksheet('reg_user_list')
        worksheet.append_row([name, email])
        print("Registration successful.")
    except Exception as e:
        print(f"An error occurred while registering: {e}")