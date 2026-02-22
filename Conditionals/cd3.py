# tea stall with diff cup sizes

price = input("Enter the size of the cup \n").lower()

if price == "small":
    print("the price of the cup is $10")
elif price == "medium":
    print("the price of the cup is $15")
elif price == "large":
    print("the price of the cup is $20")
else:
    print("Unknown cup size")