import salary_calculator as sc
import spreadsheet_operations as sp_ops
import user_reg as user_register
import ui_helpers as ui_h
def ask_restart_or_exit():
    """
    Asks the user if they want to restart the application or exit.
    """
    while True:
        choice = input("Do you want to restart the application or exit? '1)restart' or '2)exit' : ").lower().strip()
        if choice == "1":
            return True
        elif choice == "2":
            return False
        else:
            print("Invalid input. Please type '1) restart' or '2) exit' : ")


def main(): 
    while True:
        sc.clear_screen()
        sc.welcome_message()        
        is_new_user = user_register.ask_the_user("Have you used Salary Calculator before? (yes/no): ")
        sc.clear_screen()
        sc.welcome_message()
        if not is_new_user:
            user_register.register_user()
        else:
            response = user_register.check_returning_user()
            if not response : 
                sc.clear_screen()
                if not ask_restart_or_exit():
                    break
                else:
                    main()
            else :
               user_register.register_user() 
        
        
        sc.clear_screen()
        sc.welcome_message()
        user_type = sc.get_user_type()
        if user_type == '2':
            num_employees = sc.get_number_of_employees()            
            sc.welcome_message()          
            for emp_num in range(num_employees):
                sc.clear_screen()
                emp_name = sc.processing_data_input_output(user_type, emp_num)
                print("\033[32m" + f"Employee '{emp_name}' has been inserted" + "\033[0m")                
                sp_ops.reset_spreadsheet('operation_table')                
            sp_ops.print_all_user_calculated_data()
            sp_ops.reset_spreadsheet('all_users_calculated_data')
        else:
            sc.processing_data_input_output(user_type)
            sp_ops.reset_spreadsheet('all_users_calculated_data')         
            
        if not ask_restart_or_exit():
            break
    sc.clear_screen()
    sc.welcome_message()    
    ui_h.print_with_delay("Thank you for using the application!")

if __name__ == "__main__":
    main()