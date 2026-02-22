# running an online tea store

order_amount = int(input("enter the order amount"))

# ternary operator

delivery_free = 0 if order_amount > 300 else print("delivery free is rs 30")
print(delivery_free)