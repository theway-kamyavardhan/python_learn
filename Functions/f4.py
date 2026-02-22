# non local and global scopes
"""
we can access the local by calling it globally naming it as non local 
"""

def update_order():
    chai_type = "elaichi"
    def kitchen():
        nonlocal chai_type # referrign to the variable outside the function
        chai_type = "kesar"
    kitchen()
    print("after update",chai_type)

update_order()


#####OR######

chai_type = "Masala"

def chai_fav():
    global chai_type
    chai_type = "FAVVV"
    print("changing the global var",chai_type)

chai_fav()
print("Printing outside to check the variation too",chai_type)