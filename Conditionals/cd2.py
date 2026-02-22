# snack programm conditionals
snack = input("enter the snack you want \n Cookies \n Samosa ... \n").lower()

if snack == "samosa":
    cond = input("do you want this snack?")
    if cond == "yes":
        print("order taken")
    else:
        print("order cancelled")
elif snack == "cookies":
    cond = input("do you want this snack?")
    if cond == "yes":
        print("order taken")
    else:
        print("order cancelled")
else:
    print("wrong input taken")