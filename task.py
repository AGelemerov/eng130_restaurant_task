# User Stories
# 1
# As a User I want to be able to see the menu in a formatted way, so that I can order my meal.

# 2
# As a User I want to be able to order 3 times, and have my responses added to a list, so they aren't forgotten

# 3
# As a user, I want to have my order read back to me in formatted way, so I know what I ordered.
menu = {
    1: "Pizza",
    2: "Lasagne",
    3: "Linguine Carbonara",
    4: "Fettuccine Alfredo",
    5: "Risotto",
    6: "Ravioli"
}
amount_of_orders = 0
cart = []

while amount_of_orders < 3:
    for item in menu.items():
        print(str(item[0]) + ".", item[1])

    chosen_item = input("Please choose an item from the menu, 0 to end selection (number): ")
    if chosen_item == "0":
        break
    cart.append(chosen_item)
    amount_of_orders += 1

print("\nYour order is as follows: ")
for item in cart:
    print(item)
