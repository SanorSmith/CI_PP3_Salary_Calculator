def validate_input(input_value, validation_type, max_value=None):
    """
    General purpose input validation function.
    Validates the given input based on the specified validation type.

    :param input_value: The value to validate.
    :param validation_type: The type of validation ('name', 'days', 'salary', 'choice').

    """
    #Validate the number of name.
    if validation_type == "name":
        if not input_value.strip():
            raise ValueError("\033[31m" + "The name cannot be empty." + "\033[0m")
        if not input_value.replace(' ', '').isalpha():
            raise ValueError("\033[31m" + "The name must contain only letters." + "\033[0m")
        return input_value.strip()
    
    #Validate the number of days.
    elif validation_type == "days":
        if not input_value.isdigit() or not 1 <= int(input_value) <= 31:
            raise ValueError("\033[31m" + "The number of days must be between 1 and 31." + "\033[0m")
        return int(input_value)
    
    #Validate the salary amount.
    elif validation_type == "salary":
        if not input_value.isdigit() or int(input_value) < 0:
            raise ValueError("\033[31m" + "Please enter a valid integer number for salary. It cannot be negative." + "\033[0m")
        return int(input_value)

    #Validate the user's job and county choices inputs
    elif validation_type == "choice":
        if not input_value.isdigit():
            raise ValueError("\033[31m" + "Input must be a number." + "\033[0m")
        choice = int(input_value)
        if not 1 <= choice <= max_value:
            raise ValueError("\033[31m" + f"Input must be a number between 1 and {max_value}." + "\033[0m")
        return choice
    
    # Validate the choice to print out calculation results.
    elif validation_type == "choice_c_r":
        input_value = input_value.lower().strip()
        if input_value not in ['yes', 'no', 'y', 'n']:
            raise ValueError("\033[31m" + "Invalid input. Please enter (yes/no): " + "\033[0m")
        return input_value
    else:
        raise ValueError("\033[31m" + "Invalid validation type specified." + "\033[0m")
