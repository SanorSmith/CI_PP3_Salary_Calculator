
import os,time


def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system('clear')


def print_with_delay(text, delay=0.03):
    """
    Prints text with a delay after each character.

    :param text: The text to print.
    :param delay: Delay after each character, in seconds.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  


def print_centered_box(message, width=60):
    """
    Function to display a message inside a centered box with a border.
    :param message: The message to be displayed.
    :param width: The width of the box.
    """
    lines = str(message).split('\n')
    centered_lines = [line.strip().center(width - 4) for line in lines]
    separator = '+' + '-' * (width - 2) + '+'
    print(separator)
    for line in centered_lines:
        print('| ' + line + ' |')
    print(separator)
    

def welcome_message():
    """
    Function to display a welcome message to the user.
    """
    message = (
        "Welcome to the Salary Calculator program.\n\n"
        "This application assists individuals in computing\n"
        "their monthly/daily net income by utilizing mathematical\n"
        "formulas and tax data. It simplifies the process of\n"
        "calculating monthly salaries and provides accurate\n"
        "tax amounts based on county tax tables.\n\n"
        "Let's get started!"
    )   
    print_centered_box(message)    
    

def print_user_data_table(output_details):
    """
    Prints user data in a formatted table.

    :param output_details: A list of tuples containing the details to be printed.
    """
    # Print the final summary in a table format
    print_with_delay("\nFinal Summary:\n")
    print_with_delay(f" {'Detail':<40}  {'Value':<50}")
    print_with_delay("|" + "-" * 75 + "|")
    for detail in output_details:
        print_with_delay(f" {detail[0]:<40} | {str(detail[1]):<40}")
        print("|" + "-" * 75 + "|")
        