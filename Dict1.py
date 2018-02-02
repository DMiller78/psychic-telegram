fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)
# # print(fruit["lemon"])
# # dictionaries store can store a lot of different kinds of information
# # can add to a dictionary
# fruit["pear"] = "an odd shaped apple"
# fruit["lime"] = "great with tequila"
# print(fruit["pear"])
# # del fruit["lemon"] to delete lemon
# # fruit.clear()
# # print(fruit)
# print(fruit["tomato"])

print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     # fruit.has_key(dict_key)
#     # old python 2 code does not work in python 3
#     print(description)
#     # better to use it this way - default value or key value use the other program
#
#     # if dict_key in fruit:
#     #     description = fruit.get(dict_key)
#     #     print(description)
#     else:
#         print("we don't have a " + dict_key)


for snack in fruit:
    print(fruit[snack])
# the order is changing each time when you run the program - it is not constrained
# no guarantee the list will print again the same way

# dictionary is a load of free slots

