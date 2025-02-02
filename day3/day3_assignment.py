"""EXERCISE 1: Creating a Grocery List with Tuples
Goal: Get comfortable creating and working with tuples and lists
Instructions:
Define three tuples to represent grocery items, each containing:
name (string), price (float), and quantity (integer).
Example: apples_tuple = ("apples", 0.50, 5)
Create an empty grocery_list as a Python list and add each tuple to the grocery_list.
Print each item in the grocery_list individually by accessing them with indexing.
Example Output: ("apples", 0.50, 5)
Calculate the total_cost for each item using the price and quantity.
Print each item’s name and total cost.
Example Output:"""


apples_tuple = ("apples", 0.50, 5)
banana_tuple = ("banana", 0.75,6)
orange_tuple = ("orange", 0.10,10)

grocery_list = []
grocery_list.append(apples_tuple)
grocery_list.append(banana_tuple)
grocery_list.append(orange_tuple)

print(grocery_list[0])
print(grocery_list[1])
print(grocery_list[2])

print(f"Total cost of apples is ${apples_tuple[1] * apples_tuple[2]}")
print(f"Total cost of banana is ${banana_tuple[1] * banana_tuple[2]}")
print(f"Total cost of orange is ${orange_tuple[1] * orange_tuple[2]}")


"""EXERCISE 2: Working with Dictionaries
Goal: Get used to using dictionaries to store and compute data.
Instructions:
Create three dictionaries for grocery items containing the following keys:
"name" (string), "price" (float), "quantity" (integer)
Example: apple_dict = {"name":"apple", "price":0.50, "quantity": 5}
For each of the dictionaries, calculate and store the total cost by multiplying price and quantity, and assign it to a new key, "total_cost".
Expected output:
apple_dict = {"name":"apple", "price":0.50, "quantity": 5, "total_cost": 2.5}

Print the total cost for each item:
Expected Output: "Total cost of apples: $2.50"
OPTIONAL TIP:  you can force floats to use 2 decimal places by using the method round()
Example 1:
round(<the float you want to round off>, <number of decimal places>)
round(3.987654318, 2)
3.99	# Result

 	Example 2:
round(apple_dict["total_cost"], 2)
2.50  # Result

"""

apple_dict = {"name":"apple", "price":0.50, "quantity": 5}
apple_total_cost = apple_dict['price'] * apple_dict['quantity']
apple_dict['total_cost'] = apple_total_cost

print(apple_dict)
print(f"Total cost of apple is ${round(apple_dict['total_cost'])}")


durian_dict = {"name":"durian", "price":1.6798, "quantity": 5}
durian_total_cost = durian_dict['price'] * durian_dict['quantity']
durian_dict['total_cost'] = durian_total_cost

print(durian_dict)
print(f"Total cost of durian is ${round(durian_dict['total_cost'])}")

pomelo_dict = {"name":"pomelo", "price":10.99, "quantity": 6}
pomelo_total_cost = pomelo_dict['price'] * pomelo_dict['quantity']
pomelo_dict['total_cost'] = pomelo_total_cost

print(pomelo_dict)
print(f"Total cost of pomelo is ${round(pomelo_dict['total_cost'])}")

"""EXERCISE 3: Slicing and Sorting a List
Goal: Practice list slicing, sorting, and calculating list length.
Instructions:
Using the list num_list = [16, 47, 1, 3, 5, 9, 15, 2], complete the following:
Slice and print: Everything from the second index onward.
Slice and print: Everything up to (but not including) the fourth index.
Use a negative index to get and print the third-to-last item in the list.
Sort the list in descending order and print the sorted list.
Find and print the length of num_list """

num_list = [16, 47, 1, 3, 5, 9, 15, 2]
print(f"Everything from the second index onward: {num_list[1:]}")
print(f"Everything up to (but not including) the fourth index: {num_list[:4]}")
third_to_last_item = num_list[-3]
print(f"Third to the last item is {third_to_last_item }")
print(f"Lenght of the list is {len(num_list)}")


"""EXERCISE 4: Sets Operations
Goal: Use sets to store unique items and perform set operations.
Instructions:
Create two sets that contain the following:
Dairy Products: milk, butter, cream, yogurt, and cheese 
Desserts: jello, chocolate, candy, cookies, muffins 
Add the shared item, ‘ice_cream’ to both sets that qualifies as both a dessert and a dairy product
Remove an item from each set that is not the shared item
Find and print the intersection (common items) between the two sets 
Expected Output: {'ice_cream'}"""

dairy_product = {'milk', 'butter', 'cream', 'yogurt', 'cheese'}
desserts = {'jello', 'chocolate', 'candy', 'cookies', 'muffins'}

dairy_product.add("ice_cream")
desserts.add(("ice_cream"))
dairy_product.remove("cheese")
desserts.remove("candy")

common_item = dairy_product.intersection(desserts)
print(f"Common Items : {common_item}")

