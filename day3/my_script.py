# my_list = ["apple", "banana", "mango"]
# print("Hello")
# print(my_list[2])

# my_list.append("cherries")
# my_list.append("coconut")
# print(my_list)
# print(my_list[1:3])
# print(my_list[2:])
# print(my_list[:4])
# print(my_list[:-1])
# print(my_list[-1])

# my_list.reverse()
# print(my_list)
# print(my_list[::-1])

# my_tuple = (10,20,30)
# my_tuple2 = (40,50)
# print(my_tuple)

# print(my_tuple+my_tuple2)

# book = {'title': '1984', 'author': 'George Orwell', 'year': 1949}
# print(f"author: {book['author']}")

# profile = {}
# profile['name'] = 'Celine'
# profile['city'] = 'Belmont'
# print(profile)
# profile['city'] = 'London'
# print(profile)
# print(profile['city'])
# print(profile.keys())
# print(profile.values())
# print(profile.items())


# student = {'name': 'Emma', 'grade': 'A', 'subject': 'Math'}
# student.pop('subject')
# print(student.keys())
# print(student.values())

fruits ={'apple', 'banana', 'cherry'}
fruits.add('orange')
print(fruits)

fruits.remove('banana')
print(fruits)
fruits.discard('banana')

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_union = set_a.union(set_b)
print(set_union)
set_intersection = set_a.intersection(set_b)
print(set_intersection)

set_x = {'cat', 'dog', 'fish'}
set_y = {'dog', 'bird'}
set_difference = set_y.difference(set_x)
print(set_difference)