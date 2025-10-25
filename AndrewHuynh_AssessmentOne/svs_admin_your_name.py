# ============== Selwyn Vet Services MAIN PROGRAM ==============

from svs_data import col_invoices,col_customers,col_treatments,col_services,db_customers,db_treatments,db_services,unique_id,display_formatted_row   # svs_data.py MUST be in the SAME FOLDER as this file!
                    # spb_data.py contains the data
import datetime     # We are using date times for this assessment, and it is
                    # available in the column_output() fn, so do not delete this line


def check_cancel(user_input):
    # function to check if the user wants to cancel the function
    if user_input == "x" or user_input == "X":
        print("function cancelled")
        return True
    return False  # this returns if the user inputs anything else

def check_number(user_input):
    if user_input.isdigit():
        return True
    else:
        print("invalid input, please try again.")
    return False

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


def list_treatments():
    # uses col_treatments for display
    display_list = []
    for treatment in db_treatments.keys():
        display_list.append((treatment,
                             db_treatments[treatment][0],
                             db_treatments[treatment][1]
                             ))
    print("\n Treatment List\n")
    format_columns = "{: >3} | {: <15} | ${: <10}"
    display_formatted_row(list(col_treatments.keys()), format_columns)
    for row in display_list:
        display_formatted_row(row, format_columns)

    #input("\nPress Enter to continue. ")
    # List the ID, name, cost of all treatments

def list_services():
    display_list = []
    for service in db_services.keys():
        display_list.append((service,
                            db_services[service][0],
                            db_services[service][1]
                            ))
    print("\n List of Services\n")
    format_columns = "{: >4} | {: <20} | {: <10}"
    display_formatted_row(list(col_services.keys()), format_columns)
    for row in display_list:
        display_formatted_row(row, format_columns)

    #input("\nPress Enter to continue ")

    # List the ID, name, cost of all services

def add_customer():
    # Add a customer to the db_customers database, use the unique_id to get an id for the customer.
    # Remember to add all required dictionaries.

    # create a new customer id using the unique_id function
    create_new_customer = True
    while create_new_customer:
        new_customer_id = unique_id()

        print("\nPlease enter your details below")
        print("(enter 'X' to cancel)")
        print("-------------------------------")

        # request customer name
        customer_name = str(input("Please enter your name: "))
        if check_cancel(customer_name):
            return

        # request customer phone number
        customer_phone_number = str(input("Please enter your phone number: "))
        if check_cancel(customer_phone_number):
            return
        # request customer email
        customer_email = str(input("please enter your email address: "))
        if check_cancel(customer_email):
            return

        # insert the customer details into db_customers
        db_customers[new_customer_id] = {
            'details': [customer_name, customer_phone_number, customer_email],
            'bookings': {}
        }

        print("Details have been successful saved into our system")

        check_add_another = False
        while not check_add_another:
            add_another_customer = input("Do you want to add another customer? (Y or N)")
            if add_another_customer.lower() == 'n':
                return
            elif add_another_customer.lower() == 'y':
                check_add_another = True
            else:
                break

    # pause the code
    input("\nPress Enter to continue.")


def add_booking():

    # first list the customers for the user to select a customer
    list_customers()

    # check if that id exists in the system
    id_check = False
    confirmed_id = 0
    while not id_check:
        input_id = input("\nPlease enter an existing customer id (Enter X to cancel): ")
        if check_cancel(input_id):
            return

        if not check_number(input_id):
            continue

        if int(input_id) in db_customers.keys():
            print(f"Customer ID: {input_id} has been found in the system")
            confirmed_id = int(input_id)
            id_check = True
        else:
            print(f"ID: {input_id} was not found.")

    # Create booking date
    date_check = False
    confirmed_date = None
    while not date_check:
        input_date = input("Please enter the booking date (YYYY-MM-DD)(Enter X to cancel):")
        if check_cancel(input_date):
            return
        try:
            confirmed_date = datetime.datetime.strptime(input_date, '%Y-%m-%d').date()
            print(f"{confirmed_date} is a correct format please continue")
            date_check = False
            break
        except ValueError:
            print("Incorrect format. ")
    # list services
    list_services()

    # check if user input exists in the service database
    service_check = False
    confirmed_service = None
    while not service_check:
        input_service =input("Please enter a service id: (Enter X to cancel)")
        if check_cancel(input_service):
            return
        if not check_number(input_service):
            continue

        if int(input_service) in db_services.keys():
            print(f"service ID: {input_service} found.")
            confirmed_service = int(input_service)
            service_check = True
        else:
            print("service ID not found")

    # list Treatments
    list_treatments()

    # check if user input exists in the treatment database
    treatment_check = False
    confirmed_treatment = None
    while not treatment_check:
        input_treatment =input("Please enter a treatment id: (Enter X to cancel)")
        if check_cancel(input_treatment):
            return
        if not check_number(input_treatment):
            continue

        if int(input_treatment) in db_treatments.keys():
            print(f"Treatment ID: {input_treatment} found.")
            confirmed_treatment = int(input_treatment)
            treatment_check = True
        else:
            print("treatment ID not found")

    # combine the cost of treatment and service cost
    confirmed_cost = round((db_treatments[confirmed_treatment][1]+db_services[confirmed_service][1]),2) # round to 2 decimals
    confirmed_payment = False #Payment defaults to false in system

    db_customers[confirmed_id]['bookings'][confirmed_date] = [
        (confirmed_service,), # add service
        (confirmed_treatment,),
        confirmed_cost,
        confirmed_payment# add treatment
        # add combined treatment and service cost
    ]

    print(db_customers[confirmed_id]['bookings'][confirmed_date])
    input("Booking complete (click enter to continue): ")


def invoices_to_pay():

    print("--- Outstanding Invoices ---")
    format_columns = "{: <5} | {: <12} | {: <15} | {: <12} | {: <10}"
    display_formatted_row(["ID","Date", "Customer Name", "Phone Number", "Total Due"], format_columns)

    for customer_key, customer_values in db_customers.items():
        customer_id = customer_key
        customer_name = customer_values['details'][0]
        customer_phone_number = customer_values['details'][1]
        for booking_date, booking_values in customer_values['bookings'].items():
            payment_check = booking_values[3]
            total_cost = booking_values[2]
            if not payment_check:
                display_formatted_row((
                    customer_id,
                    booking_date,
                    customer_name,
                    customer_phone_number,
                    f"${total_cost}"), format_columns
                )

    # Pause the code to allow the user to see output


# date customer phone and cost
def pay_invoice():
    invoices_to_pay()
    # select customer ID
    id_check = False
    correct_id = None
    while not id_check:
        input_id = input("Please enter customer ID (Enter X to cancel): "
                         )
        if check_cancel(input_id):
            return
        if not check_number(input_id):
            continue

        # check if this customer id exists
        if int(input_id) in db_customers.keys():
            correct_id = int(input_id)
            id_check = True
        else:
            print("invalid customer ID")
            return

        # check if the customer_id has any paid bookings
        for booking_date, booking_values in db_customers[correct_id]['bookings'].items():
            if booking_values[3]:
                print(f"Customer ID: {correct_id} has already paid for this booking date")
                return

    # select customer booking date
    booking_date_check = False
    correct_date = None
    while not booking_date_check:
        input_date = input("Please enter the booking date (YYYY-MM-DD)(Enter X to cancel):")
        if check_cancel(input_date):
            return
        try:
            correct_date = datetime.datetime.strptime(input_date, '%Y-%m-%d').date()
            print(f"{correct_date} is a correct format")
            booking_date_check = False
            if correct_date not in db_customers[correct_id]['bookings'].keys():
                print("invalid booking date")
                continue
            break
        except ValueError:
            print("Incorrect format. ")
            continue

    print("payment has been updated")
    db_customers[correct_id]['bookings'][correct_date][3] = True

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
while response.lower() != "x":
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
