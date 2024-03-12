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