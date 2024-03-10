#Validate User input data function 

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
            raise ValueError("The name cannot be empty.")
        if not input_value.replace(' ', '').isalpha():
            raise ValueError("The name must contain only letters.")
        return input_value.strip()
    
    #Validate the number of days.
    elif validation_type == "days":
        if not input_value.isdigit() or not 1 <= int(input_value) <= 31:
            raise ValueError("The number of days must be between 1 and 31.")
        return int(input_value)
    
    #Validate the salary amount.
    elif validation_type == "salary":
        salary = int(input_value)
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        return salary

    #Validate the user's job and county choices inputs
    elif validation_type == "choice":
        if not input_value.isdigit():
            raise ValueError("Input must be a number.")
        choice = int(input_value)
        if not 1 <= choice <= max_value:
            raise ValueError(f"Input must be a number between 1 and {max_value}.")
        return choice
    
    # Validate the choice to print out calculation results.
    elif validation_type == "choice_c_r":
        input_value = input_value.lower().strip()
        if input_value not in ['yes', 'no', 'y', 'n']:
            raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
        return input_value
    else:
        raise ValueError("Invalid validation type specified.")
