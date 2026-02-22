# scope and namespace in functions
#name resolution and scope is same 

# we have local , enclosing and global variables and another is built in 

def serve_chai():
    chai_type = " masala chai"# local scope within the function
    print(chai_type)

chai_type = " Lemon" # this is a global
serve_chai()
print(f"{chai_type} this is the outer one")


# now for the another one this is the enclosing one 
def chai_counter():
    chai_order = "lemon" # enclosing scope
    def print_order():
        chai_order = "ginger"
        print("INNER:",chai_order)
    print_order()
    print("Outer:",chai_order)

chai_counter()

