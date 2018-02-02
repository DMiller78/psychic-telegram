fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

# order_key = list(fruit.keys())
# order_key.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])


# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' * 40)

# for f in sorted(fruit.keys()):
# for f in fruit:
#     print(f + " - " + fruit[f])
# for val in fruit.values():
#     print(val)
#
# print('-' * 40)
#
# for key in fruit:
#     print(fruit[key])


fruit_keys = fruit.keys()
print(fruit_keys)

fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)

# print(fruit.values())
# both are called valued objects


