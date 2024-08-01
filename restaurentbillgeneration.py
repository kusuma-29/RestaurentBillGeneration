from datetime import datetime

name = input("Enter your name: ")
print("All Types Of Biriyani Items!!!!")
menu = '''
Chicken Biriyani   rs 250
Mutton Biriyani    rs 800
Fish Biriyani      rs 600
Prawns Biriyani    rs 500
Veg Biriyani       rs 90
Boneless Biriyani  rs 190
Chicken65          rs 300
Cooling Water Bottle rs 40
Dhumsup              rs 30
Sprit                rs 30
Mountain Due         rs 40
Mazza                rs 40
Merinda              rs 40
CocoCola             rs 30
Limca                rs 30
'''
items = {
    "Chicken Biriyani": 250,
    "Mutton Biriyani": 800,
    "Fish Biriyani": 600,
    "Prawns Biriyani": 500,
    "Veg Biriyani": 90,
    "Boneless Biriyani": 190,
    "Chicken65": 300,
    "Cooling Water Bottle": 40,
    "Dhumsup": 30,
    "Sprit": 30,
    "Mountain Due": 40,
    "Mazza": 40,
    "Merinda": 40,
    "CocoCola": 30,
    "Limca": 30
}

price_list = []
total_price = 0

option = int(input("Enter 1 for list of items: "))
if option == 1:
    print(menu)

for _ in range(len(items)):
    input1 = int(input('If you want to buy items press 1 or 2 for exit: '))
    if input1 == 2:
        break
    if input1 == 1:
        item = input("Enter item: ").strip()  # Strip any leading/trailing spaces
        quantity = int(input("Enter the quantity: "))
        if item in items:
            price = quantity * items[item]
            price_list.append((item, quantity, price))
            total_price += price
        else:
            print("Item is not available")
    else:
        print("Invalid input. Please enter 1 to buy items or 2 to exit.")
        continue

ac_charge = 0
ac_charge_type = ""

dining_option = input("Are you dining in or taking a parcel? (Enter 'dine' or 'parcel'): ").strip().lower()
if dining_option == 'dine':
    ac_option = input("Do you want AC or non-AC? (Enter 'ac' or 'non-ac'): ").strip().lower()
    if ac_option == 'ac':
        ac_charge = 500
        ac_charge_type = "Room bill for AC"
    else:
        ac_charge = 200
        ac_charge_type = "Room bill for Non-AC"

tip_amount = float(input("Enter tip amount in rupees: "))
final_amount = total_price + tip_amount + ac_charge

inp = input("Can I print the bill? (yes or no): ").strip().lower()
if inp == 'yes' and final_amount != 0:
    print(25 * '*', 'Halal Biryani Point', 54* '*')
    print(25 * '=', 'Barampet, Narasaraopet - 522601 (Opposite to Stadium First Gate)', 9 * '=')
    print(25 * '=', 'Timings: Mon-Sun: 10:00 am-11:00 pm', 37 * '=')
    print(25 * '=', 'Contact Information: 7947428830', 41* '=')
    print('Name:', name, 30 * '=', 'Date:', datetime.now())
    print(100 * '=')
    print('{:<4} {:<20} {:<10} {:<10}'.format('Sno', 'Item', 'Quantity', 'Price'))
    for i in range(len(price_list)):
        item, quantity, price = price_list[i]
        print('{:<4} {:<20} {:<10} {:<10}'.format(i + 1, item, quantity, price))
    print(100* '-')
    print(50 * ' ', 'Total amount:', 'rs', total_price)
    print(50 * ' ', 'Tip amount:', 'rs', round(tip_amount, 2))
    if ac_charge > 0:
        print(50 * ' ', ac_charge_type + ':', 'rs', ac_charge)
    print(100 * '-')
    print(50 * '-', 'Final amount:', 'rs', round(final_amount, 2))
    print(100 * '-')
    print(25 * '*', 'Thankuuu For Visiting Us!', 47* '*')
else:
    print("Thank you for visiting!")
