import salary_calculator as sc
import spreadsheet_operations as sp_ops

def ask_restart_or_exit():
    """
    Asks the user if they want to restart the application or exit.
    """
    while True:
        choice = input("Do you want to restart the application or exit? (1:restart/2:exit): ").lower().strip()
        if choice == "1":
            return True
        elif choice == "2":
            return False
        else:
            print("Invalid input. Please type 'restart' or 'exit'.")


def main(): 
    while True:
        sc.clear_screen()
        sc.welcome_message()
        user_type = sc.get_user_type()
        if user_type == '2':
            num_employees = sc.get_number_of_employees()
            for emp_num in range(num_employees):
                sc.processing_data_input_output(user_type, emp_num)
                print(f"Employee {emp_num+1} has been inserted")
                sp_ops.reset_spreadsheet()
        else:
            sc.processing_data_input_output(user_type)
            sp_ops.reset_spreadsheet()         
            
        if not ask_restart_or_exit():
            break
    print("Thank you for using the application!")

if __name__ == "__main__":
    main()