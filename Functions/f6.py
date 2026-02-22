# Handling multiple return in python
def make_chai():
    print("hey this should be printed")

return_value = make_chai()

print(return_value)

# here as we know nothing is getting printed because the return value is storing the make chai funciton but not returning the object wihtin
# thats why it is returning nothing to none

