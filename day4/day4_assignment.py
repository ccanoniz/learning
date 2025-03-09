#EXERCISE 1: Grocery Item Categorization Using 

food_items = ["apple", "bread", "milk"]
non_food_items = ["soap", "detergent", "paper towels"]

input_grocery_item = input("Enter an item from the grocery: ")

if input_grocery_item in food_items:
    print (f"{input_grocery_item} is classified as food_items")
elif input_grocery_item in non_food_items:
    print (f"{input_grocery_item} is classified as non_food_items")
else:
    print (f"{input_grocery_item} is classified as UNKNOWM")


#EXERCISE 2: Making a Burger with a While Loop
"""
You want to make burgers and fries for you and your friends, but you only have $27.50. Let’s see if we can make burgers and fries with our budget.

From the given list of dictionaries:
Create a variable called shopping_list that stores an empty list:
Create a variable called budget that stores our budget
Create a variable called total_cost with the value of zero
Create a variable called index that will store the current index starting from 0
Create a while loop that runs while the total cost is less than or equal to the budget
Under the while loop create a variable called item that gets the item at the current index from the items_list
Add the item name to the shopping list
Add the item cost to the total cost by calculating the cost multiplied by the amount
Add one to the index
Outside of the while loop, print the shopping list
Expected output: ['fries', 'burger patties', 'burger buns', 'tomato']"""


shopping_list = []
budget = 27.50
total_cost = 0 
index = 0


items_list = [
    {"name": "fries", "cost":6.25, "amount": 1},
    {"name": "burger patties", "cost":13.50, "amount": 1},
    {"name": "burger buns", "cost":3.50, "amount": 2},
    {"name": "tomato", "cost":1.50, "amount": 2},
    {"name": "lettuce", "cost":5, "amount": 1},
    {"name": "Ketchup", "cost":3.47, "amount": 1},
    {"name": "pickles", "cost":4.25, "amount": 1}
]

while total_cost <= budget and index < len(items_list):

    current_item = items_list[index]
    item_cost = current_item['cost'] * current_item['amount']

    if total_cost + item_cost > budget:
        break

    shopping_list.append(current_item['name'])
    total_cost +=item_cost
    index+=1

print(shopping_list)

#EXERCISE 3: Extending Logic with Nesting
shopping_list = []
budget = 27.50
total_cost = 0 
index = 0


items_list = [
    {"name": "fries", "cost":6.25, "amount": 1},
    {"name": "burger patties", "cost":13.50, "amount": 1},
    {"name": "burger buns", "cost":3.50, "amount": 2},
    {"name": "tomato", "cost":1.50, "amount": 2},
    {"name": "lettuce", "cost":5, "amount": 1},
    {"name": "Ketchup", "cost":3.47, "amount": 1},
    {"name": "pickles", "cost":4.25, "amount": 1}
]

while total_cost <= budget and index < len(items_list):

    current_item = items_list[index]
    item_cost = current_item['cost'] * current_item['amount']

    if total_cost + item_cost > budget:
        break

    shopping_list.append(current_item['name'])
    total_cost +=item_cost
    index+=1

    item = 0 
    for item in shopping_list:
        print (item)
    print("----------------")
        
print(shopping_list)



#EXERCISE 4: Breaking the Loop
"""
Goal: Get comfortable controlling loops and breaking them when they meet your conditions
Instructions:
Technically, to make burgers and fries we only really need burger buns, fries, and burger patties. Let’s say our friends are bringing all the condiments.
After we have printed all the shopping list items, check if burger buns are in the shopping list and if fries are in the shopping list and if burger patties are in the shopping list
Hint: We can use logical operators here
If these conditions are true, print “We can make burgers and fries for (total cost)!” and then break the while loop
Expected output:
fries
------------
fries
burger patties
------------
fries
burger patties
burger buns
------------
We can make burgers and fries for 26.75!
['fries', 'burger patties', 'burger buns']

"""


shopping_list = []
budget = 27.50
total_cost = 0 
index = 0


items_list = [
    {"name": "fries", "cost":6.25, "amount": 1},
    {"name": "burger patties", "cost":13.50, "amount": 1},
    {"name": "burger buns", "cost":3.50, "amount": 2},
    {"name": "tomato", "cost":1.50, "amount": 2},
    {"name": "lettuce", "cost":5, "amount": 1},
    {"name": "Ketchup", "cost":3.47, "amount": 1},
    {"name": "pickles", "cost":4.25, "amount": 1}
]

necessary_items = ["burger buns", "fries", "burger patties"]


while total_cost <= budget and index < len(items_list):

    current_item = items_list[index]
    item_cost = current_item['cost'] * current_item['amount']

    if total_cost + item_cost > budget:
        break

    shopping_list.append(current_item['name'])
    total_cost +=item_cost
    index+=1

    item = 0 
    for item in shopping_list:
        print (item)
    print("----------------")

    if all(item in shopping_list for item in necessary_items):
        print(f"We can make burgers and fries for {total_cost}!")
        break  # Stop the loop once we have the necessary items

        
print(shopping_list)


#EXERCISE 5: Error Handling with Try-Except

"""
Goal: Get used using try-except blocks to handle errors
Instructions:
What happens when we change the index to a string? This should give you an error:
Inside the while loop, add a try-except block to catch the error and print a useful message to the user so that the error doesn’t occur. 
Add a break after printing the message
This is because if we have an error we don’t  want to go through the rest of the code
Expected output:
ERROR: The index must be an integer
[]
"""
shopping_list = []
budget = 27.50
total_cost = 0 
index = 0

items_list = [
    {"name": "fries", "cost": 6.25, "amount": 1},
    {"name": "burger patties", "cost": 13.50, "amount": 1},
    {"name": "burger buns", "cost": 3.50, "amount": 2},
    {"name": "tomato", "cost": 1.50, "amount": 2},
    {"name": "lettuce", "cost": 5, "amount": 1},
    {"name": "Ketchup", "cost": 3.47, "amount": 1},
    {"name": "pickles", "cost": 4.25, "amount": 1}
]

necessary_items = ["burger buns", "fries", "burger patties"]

while total_cost <= budget and index < len(items_list):
    try:
        # Try to access the current item
        current_item = items_list[index]
        item_cost = current_item['cost'] * current_item['amount']

        if total_cost + item_cost > budget:
            break

        shopping_list.append(current_item['name'])
        total_cost += item_cost
        index += 1

        # Simulate an error by intentionally setting index to a string
        if index == 2:  # Trigger the error when index reaches 2
            index = "string"  # Set index to a string to simulate an error

        # Try to access the next item, which should now cause an error
        current_item = items_list[index]  # This will cause a TypeError when index is a string

        # Print items in shopping list
        for item in shopping_list:
            print(item)
        print("----------------")

        # Check if we have all necessary items
        if all(item in shopping_list for item in necessary_items):
            print(f"We can make burgers and fries for {total_cost}!")
            break  # Stop the loop once we have the necessary items

    except TypeError as e:
        # Handle the TypeError when index is not an integer
        print(f"ERROR: The index must be an integer. Error is: {e}")
        break  # Break the loop after catching the error

print(shopping_list)

#EXERCISE 6: Customize Your Script
shopping_list = []
budget = 27.50
total_cost = 0 
index = 0


items_list = [
    {"name": "pancake", "cost":2.50, "amount": 1},
    {"name": "sausage", "cost":3.00, "amount": 1},
    {"name": "egg", "cost":1.50, "amount": 2},
    {"name": "bacon", "cost":1.50, "amount": 2},
    {"name": "toast", "cost":3.00, "amount": 1},
    {"name": "Ketchup", "cost":3.47, "amount": 1},
    {"name": "coffee", "cost":4.25, "amount": 1}
]

necessary_items = ["pancake", "sausage", "egg", "bacon"]


while total_cost <= budget and index < len(items_list):

    current_item = items_list[index]
    item_cost = current_item['cost'] * current_item['amount']

    if total_cost + item_cost > budget:
        break

    shopping_list.append(current_item['name'])
    total_cost +=item_cost
    index+=1

    item = 0 
    for item in shopping_list:
        print (item)
    print("----------------")

    if all(item in shopping_list for item in necessary_items):
        print(f"We can make breakfast meal for {total_cost}!")
        break  # Stop the loop once we have the necessary items

        
print(shopping_list)