# tuples are used with ()
# these are immutable 

masala_spices = ("chai","ginger","cardomom")

# this gives us a boolean answer and we are able to test the memebership of the elements through it 
print("masala" in masala_spices)

ginger_r , masala_r = 2, 1
#by this we are able to assign to variables together without thinking about assigning two times
# we are able to do so because of tuple as we can assign tuple like this too

# we are able to assing variable to each element of the tuple
(spice1,spice2,spice3) = masala_spices
print(spice1)

#we can have a fresh memory reference but tuple cannot be changed and thats why we use list
