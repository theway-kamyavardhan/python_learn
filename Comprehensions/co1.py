# we can do work through loops too but it is more of a stylised way doing things
# we can filter item , transform item or create a new collection or flatten a nested strucuture

# starting with list comprehension

"""
its like [expression for items in iterables if condition]
"""
menu = [
    "Masala chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea]

print(iced_tea)