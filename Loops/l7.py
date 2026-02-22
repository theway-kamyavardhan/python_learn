# dictionary in repeated cases with get method

users = [
    {"id":1,"total":100,"coupon":"P20"},
    {"id":2,"total":150,"coupon":"F20"},
    {"id":3,"total":300,"coupon":"S20"},
]

discounts = {
    "P20" : (0.2,0),
    "F20" : (0.5,0),
    "S20" : (0,10)
    }

#now in the discount one has one percent discount another is the flat one 

for user in users:
    percent , flat = discounts.get(user["coupon"],(0,0))
    # putting 0,0 is for default value if nothing is there
    discount = user["total"] * percent + flat
    print(f"{user["id"]} paid {user["total"]} and got this discount rs {discount}")

# by using the get we are able to get things from different dict and able to use them together
