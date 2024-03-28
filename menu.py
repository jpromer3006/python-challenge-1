# Menu Dictionary
menu = {
    "Appetizers": {
        "Chicken nuggets": 0.99,
        "Wings": 3.69,
        "House Salad": 2.49,
        "French fries": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Cheese Pizza": 8.99,
        "Pepperoni Pizza": 10.99,
        "Vegetarian Pizza": 9.99,
        "Chicken Burger": 7.49,
        "Beef Burger": 8.49
    },
    "Drinks": {
        "Small Soda": 1.99,
        "Medium Soda": 2.49,
        "Large Soda": 2.99,
        "Green Tea": 2.49,
        "Thai Iced Tea": 3.99,
        "Irish Breakfast Tea": 2.49,
        "Espresso": 2.99,
        "Flat White": 2.99,
        "Iced Coffee": 3.49
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "New York Cheesecake": 4.99,
        "Strawberry Cheesecake": 6.49,
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Initialize order list
order_list = []

# Welcome message
print("Welcome to AI's International Food Truck. Where we travel so you don't have to.")

# Continuous loop for taking orders
while True:
    # Display menu categories
    print("\nMay I prepare one of our exquisite items you?")
    for index, category in enumerate(menu.keys(), start=1):
        print(f"{index}: {category}")
    
    # Ask for menu selection
    menu_selection = input("Please select a menu category by entering its number: ")
    
    # Check if the input is a valid number
    if menu_selection.isdigit():
        menu_index = int(menu_selection)
        
        # Check if the input is within the range of menu categories
        if 1 <= menu_index <= len(menu):
            menu_category_name = list(menu.keys())[menu_index - 1]
            print(f"\nYou selected {menu_category_name}.")
            
            # Display menu items for the selected category
            print(f"\nHere are the items available in {menu_category_name}:")
            print("Item # | Item name                 | Price")
            print("----------------------------------------")
            
            for i, (item_name, item_price) in enumerate(menu[menu_category_name].items(), start=1):
                print(f"{i:<7} | {item_name:<25} | ${item_price}")
            
            # Ask for item selection
            item_selection = input("Please enter the item number you would like to order: ")
            
            # Check if the input is a valid number
            if item_selection.isdigit():
                item_index = int(item_selection)
                
                # Check if the input is within the range of menu items
                if 1 <= item_index <= len(menu[menu_category_name]):
                    selected_item = list(menu[menu_category_name].items())[item_index - 1]
                    item_name = selected_item[0]
                    item_price = selected_item[1]
                    
                    if isinstance(item_price, dict):  # If the item has nested options
                        print(f"\nYou selected '{item_name}'.")
                        print("Available options:")
                        for option, price in item_price.items():
                            print(f"{option}: ${price}")
                        
                        # Ask for the specific option
                        option_selection = input("Please enter the option number you would like to order: ")
                        option_index = option_selection.strip()
                        if option_index in item_price:
                            item_name = f"{item_name} - {option_index}"
                            item_price = item_price[option_index]
                        else:
                            print("Invalid option.")
                            continue
                    
                    # Ask for the quantity
                    quantity = input(f"How many '{item_name}' would you like to order? (Default is 1): ")
                    quantity = int(quantity) if quantity.isdigit() else 1
                    
                    # Add the order to the order list
                    order_list.append({"Item name": item_name, "Price": item_price, "Quantity": quantity})
                    print("Your order has been added to the list.")
                else:
                    print("Invalid item number. Please try again.")
            else:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid menu category number. Please try again.")
    else:
        print("Invalid input. Please enter a number.")
    
    # Ask if the customer wants to continue ordering
    keep_ordering = input("Excellent choice would you like to pair that with anything else? (yes/no): ").lower()
    match keep_ordering:
        case 'y' | 'yes':
            continue
        case 'n' | 'no':
            print("Your order has been placed. Please review below")
            break
        case _:
            print("Invalid input. Please try again.")

# Print the order summary
if order_list:
    print("\nOrder Summary:")
    print("Item name                     1 | Price  | Quantity")
    print("------------------------------------------------")
    for order in order_list:
        item_name = order["Item name"]
        item_price = order["Price"]
        quantity = order["Quantity"]
        space1 = " " * (30 - len(item_name))
        space2 = " " * (7 - len(str(item_price)))
        print(f"{item_name}{space1}| ${item_price:.2f}{space2}| {quantity}")
    
    # Calculate and print the total cost using list comprehension
    total_cost = sum(order["Price"] * order["Quantity"] for order in order_list)
    print("-----------------------------------------------")
    print(f"\nTotal cost: ${total_cost:.2f}")
else:
    print("No items were ordered.")
    
print("\nThank you for coming to AI Food Truck. Please come again. Beep, Bop, Beep!")