# number = int(input("Give me a number:"))

# if number % 2 == 0:
#     print(f"Inputted number : ${number} is an EVEN number")
# else:
#     print(f"Inputted number : ${number} is an ODD number")
    

# temperature = int(input("What is the temperature:"))
# weather_condition = ""

# if temperature < 15:
#     weather_condition = 'COLD'
# elif temperature >=15 and temperature <=25: 
#    weather_condition = 'WARM'
# else:
#     weather_condition = 'HOT'

# print(f"The weather condition is {weather_condition}")


# age = int(input("How old are you:"))

# citizenship = input("Are you a citizen? (yes/no): ").lower()



# if age > 18: 
#     if citizenship == 'yes':
#        print("You are eligible to vote")
#     else:
#        print("You are not eligible to vote due to your citizenship")
# else:
#    print("You are not eligible to vote due to age")

# grocery_list = ['milk', 'apple', 'bread', 'banana']


# while True: 
#     add_item = input("Enter an item to add in the list or type done:")
#     if add_item == 'done':
#         break
#     grocery_list.append(add_item)


# for item in grocery_list:
#     print(f"Printing item : {item}")


grocery_list = [1,2,3,4,5,6,7,8,9,10]

# for num in grocery_list: 
#     if num > 7:
#         break
#     print(f"Number less than 7 : {num}")


# for num in grocery_list:
#     if num % 2 == 0: 
#         continue 
#     print(f"Not Even Number: {num}")


# for num in grocery_list:
#     if num % 2 == 0: 
#         pass 
#     print(f"Not Even Number: {num}")




# try:
#     num = int(input("Enter a number:"))
# except ValueError as e:
#     print(f"Please enter a number. Encouncered as error {e}")


a = 10
b = 5

# Step 1: Attempt to double the value of 'b' by assigning it to 'double_b'
# double_b = b * "2"

# # Step 2: Try to add 'a' and 'double_b' and store the result in 'total'
# total = a + double_b

# print("The total is:", total)

try: 
    double_b = b * "2"
    total = a + double_b
    print("The total is:", total)
except TypeError as e :
    print(f"Error encountered: {e}")

   


           

