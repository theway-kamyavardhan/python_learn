chai_type = "ginger chai"
# it is a string

print(f"Order for {chai_type}")

chai_description = "Aromatic and Bold"
#slicing

#last number is not inclusive
print(chai_description[0],chai_description[-1])


# reversing a string with slicing
chai = "this is in r🚫everse"
print(f"{chai} this is in reverse {chai[::-1]}")

#for special character and symbols we use encode
encoded = chai.encode("utf-8")
print(encoded)


decoded = encoded.decode("utf-8")
print(decoded)

# we learn about slicing , indexing and encoding

