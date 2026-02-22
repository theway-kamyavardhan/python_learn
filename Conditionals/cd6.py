# Building a ticket info system for a railway app
# using match case

category = int(input("\n Enter the category for train \n 1.sleeper \n 2,AC \n 3,general \n 4.luxury \n"))

match category:
    case 1:
        print("sleeper is your catgory choosen")
    case 2 :
        print("Ac is the category")
    case 3 :
        print("general")
    case 4 :
        print("luxury")
    case _:
        print("invalid seat case")