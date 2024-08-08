# Restaurent Bill Generation Using Python

The code is a simple console-based application for a restaurant called "Halal Biryani Point". It allows a user to view a menu, place an order, and get a printed bill including dining options and tips.


# Detailed Explanation


# User Input And Menu Display

The code starts by asking the user for their name.

It displays a list of biryani items along with their prices.

The menu is defined as a string and the items are stored in a dictionary with their respective prices.


# Order Processing

The user is prompted to choose if they want to see the list of items by entering 1.
A loop runs for each item in the dictionary, asking the user if they want to buy an item or exit.
If the user chooses to buy, they are prompted to enter the item name and quantity.
The code checks if the item is in the dictionary, calculates the price, and adds it to the order list and total price.
If the item is not available, it notifies the user.


# Dinning Options

The user is asked if they are dining in or taking a parcel.
If dining in, they are asked if they prefer AC or non-AC, which adds respective charges to the total bill.

# Tip And Final Amount

The user is prompted to enter the tip amount.
The final amount is calculated by adding the total price of items, tip amount, and any AC/non-AC charges.

# Bill Printing

The user is asked if they want to print the bill.
If yes, the bill is printed with the restaurant's information, user's name, date, and details of the items ordered, including quantities and prices.
The bill also shows the total amount, tip amount, and any additional charges (AC/non-AC).
Finally, the final amount is displayed and a thank you message is printed.

# Key Points

Data Storage: Menu items and prices are stored in a dictionary.
User Interaction: Multiple inputs are taken from the user for ordering, dining options, and tip amount.
Condition Handling: The code handles various conditions like invalid inputs, unavailable items, and whether to print the bill or not.
Formatted Output: The bill is printed in a formatted manner, making it easy to read and understand.











