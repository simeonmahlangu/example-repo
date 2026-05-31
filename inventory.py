
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code    
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):        
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        # this method will return the cost of the shoe
        return self.cost

    def get_quantity(self):        
        '''
        Add the code to return the quantity of the shoes.
        '''     
        return self.quantity

    def __str__(self):
        # Add a code to return a string representation of a class.
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
        
    try:
        lines = []
        with open("C:\\Users\\SimeonM\\Documents\\GitHub\\AI & Software Engineering Bootcamp\\SM26040020114\\Level 1 - Foundations of AI Engineering\\M03T07 – OOP – Synthesis\\Code Files\\inventory.txt", "r") as file:
        # Read all lines from the file into 'lines'

            lines = file.readlines()
            for line in lines:
                if line.startswith("Country"):  # Skip the header line
                    continue   
                line = line.split(",")  # Split the line into components based on the comma delimiter 
                shoe = Shoe(line[0], line[1], line[2], float(line[3]), int(line[4]))
                shoe_list.append(shoe)
    except FileNotFoundError:
            print("Error: File was not found.")

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    # Capture shoe details from user input
    country = input("Enter the country of the shoe: ")
    code = input("Enter the code of the shoe: ")
    product = input("Enter the product name of the shoe: ")
    cost = float(input("Enter the cost of the shoe: "))
    quantity = int(input("Enter the quantity of the shoe: "))

    # Create a new shoe object and add it to the list
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)

def view_all(shoe_list):
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    if not shoe_list:
            print("No shoes available.")
            return

    print("Available Shoes:")
    print(len(shoe_list), "shoes found.")
    for i, shoe in enumerate(shoe_list, start=1):
        _str_ = shoe.__str__()
        print(f"{i}. {_str_}")

def re_stock():
    
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # Find the shoe with the lowest quantity and prompt the user to restock it
    if not shoe_list:
        print("No shoes available.")
        return
    lowest_quantity_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"The shoe with the lowest quantity is: Country: {lowest_quantity_shoe.country}, Code: {lowest_quantity_shoe.code}, Product: {lowest_quantity_shoe.product}, Cost: {lowest_quantity_shoe.cost}, Quantity: {lowest_quantity_shoe.quantity}.")
    restock_choice = input("Do you want to restock this shoe? (yes/no): ")
    if restock_choice.lower() == "yes":
        additional_quantity = int(input("Enter the quantity to add: "))
        lowest_quantity_shoe.quantity += additional_quantity
        print(f"Updating quantity for {lowest_quantity_shoe.product} to {lowest_quantity_shoe.quantity}")
        with open("C:\\Users\\SimeonM\\Documents\\GitHub\\AI & Software Engineering Bootcamp\\SM26040020114\\Level 1 - Foundations of AI Engineering\\M03T07 – OOP – Synthesis\\Code Files\\inventory.txt", "w") as inventory_file:
   
            for shoe in shoe_list:             
                if shoe.code == lowest_quantity_shoe.code.upper():
                    shoe.quantity = lowest_quantity_shoe.quantity
                    inventory_file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{lowest_quantity_shoe.quantity}\n")
                    print(f"{shoe.code}'s quantity updated to {lowest_quantity_shoe.quantity}")

                else:
                    inventory_file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

           
def search_shoe(shoe_list):  
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    code = input("Enter the code of the shoe to search for: ")
    for shoe in shoe_list:
            if shoe.code == code:
                print(f"Shoe found: Country: {shoe.country}, Code: {shoe.code}, Product: {shoe.product}, Cost: {shoe.cost}, Quantity: {shoe.quantity}")
                return shoe

    print(f"No shoe found with code '{code}'.")
    return None

def value_per_item():
    
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    # Calculate and print the total value for each shoe
    if not shoe_list:
        print("No shoes available.")
        return  
    print("Shoe Values:")
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Country: {shoe.country}, Code: {shoe.code}, Product: {shoe.product}, Value: {value}")   
        

def highest_qty():
    # Get Product with the highest quantity and print it as being for sale
    if not shoe_list:
        print("No shoes available.")
        return
    highest_quantity_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"The shoe with the highest quantity is: Country: {highest_quantity_shoe.country}, Code: {highest_quantity_shoe.code}, Product: {highest_quantity_shoe.product}, Cost: {highest_quantity_shoe.cost}, Quantity: {highest_quantity_shoe.quantity}.\n This shoe is for sale!")
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
# View all shoes
read_shoes_data()
print(
    '''Welcome to the Shoe Inventory Management System!
Please select an option from the menu below:'''
)
while True:
    user_choice = input(
        """\n1. View all shoes 
2. Capture a new shoe
3. Re-stock a shoe
4. Search for a shoe
5. Calculate value per item
6. View shoe with highest quantity
7. Exit
Enter selection: """
    )

    if user_choice == "1":
        view_all(shoe_list)
    elif user_choice == "2":
        capture_shoes()
    elif user_choice == "3":
        re_stock()
    elif user_choice == "4":
        search_shoe(shoe_list)
    elif user_choice == "5":
        value_per_item()
    elif user_choice == "6":
        highest_qty()
    elif user_choice == "7":
        print("Exiting the program.")
        break
    else:
        print("Invalid selection. Please try again.")