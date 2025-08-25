# ============== Selwyn Vet Services MAIN PROGRAM ==============
# Student Name: Joana
# Student ID : 
# NOTE: Make sure your two files are in the same folder
# =================================================================================

from svs_data import col_invoices,col_customers,col_treatments,col_services,db_customers,db_treatments,db_services,unique_id,display_formatted_row   # svs_data.py MUST be in the SAME FOLDER as this file!
                    # spb_data.py contains the data
import datetime     # We are using date times for this assessment, and it is
                    # available in the column_output() fn, so do not delete this line


def list_customers():
    # List the ID, name, telephone number, and email of all customers
    # Use col_Customers for display
   
    # Convert the dictionary data into a list that displays the required data fields
    #initialise an empty list which will be used to pass data for display
    display_list = []
    #Iterate over all the customers in the dictionary
    for customer in db_customers.keys():
        #append to the display list the ID, Name, Telephone and Email
        display_list.append((customer,
                             db_customers[customer]['details'][0],
                             db_customers[customer]['details'][1],
                             db_customers[customer]['details'][2]))
    format_columns = "{: >4} | {: <15} | {: <12} | {: ^12}"
    print("\nCustomer LIST\n")    # display a heading for the output
    display_formatted_row(list(col_customers.keys()), format_columns)
    for row in display_list:
        display_formatted_row(row, format_columns)   # An example of how to call column_output function

    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output



def list_treatments():
    # List the ID, name, cost of all treatments
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def list_services():
    # List the ID, name, cost of all services
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def add_customer():
    # Add a customer to the db_customers database, use the unique_id to get an id for the customer.
    # Remember to add all required dictionaries.

    pass  # REMOVE this line once yourts have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def add_booking():
    # Add a booking to a customer
    # Remember to validate treatment and service ids
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def invoices_to_pay():
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def pay_invoice():
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

# function to display the menu
def disp_menu():
    print("==== WELCOME TO SELWYN VET SERVICES ===")
    print(" 1 - List Customers")
    print(" 2 - List Services")
    print(" 3 - List Treatments")
    print(" 4 - Add Customer")
    print(" 5 - Add Booking")
    print(" 6 - Display Unpaid Invoices")
    print(" 7 - Pay Invoice")
    print(" X - eXit (stops the program)")


# ------------ This is the main program ------------------------

# Display menu for the first time, and ask for response
disp_menu()
response = input("Please enter menu choice: ")

# Don't change the menu numbering or function names in this menu
# Repeat this loop until the user enters an "X"
while response != "X":
    if response == "1":
        list_customers()
    elif response == "2":
        list_services()
    elif response == "3":
        list_treatments()
    elif response == "4":
        add_customer()
    elif response == "5":
        add_booking()
    elif response == "6":
        invoices_to_pay()
    elif response == "7":
        pay_invoice()
    else:
        print("\n***Invalid response, please try again (enter 1-7 or X)")

    print("")
    disp_menu()
    response = input("Please select menu choice: ")

print("\n=== Thank you for using Selywn Vet Services! ===\n")
