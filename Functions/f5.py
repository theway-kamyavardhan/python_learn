# the parameters values are the arguements 
chai1 = "masala chai"

def chai(order):
    print("chai is prepared",order)

chai(chai1)

# here we can see the order variable takes the chai1 as value and pass this as the argument
# we have args and *kwargs

def special_chai ( *indegredients , **extras):
    print("Indegredients",indegredients)
    print("Extras",extras)

special_chai("cinnamon","cardomom",sweetner = "honey",foam="thick")
#so whatever is in the indegredients but if we are adding anything other than the variable given it takes all the value 
#within the extras