# take names for list of names and then order

N = int(input("Enter the number of names to take order for:"))
ls = []
for i in range(0,N):
    name = input()
    ls.append(name)

for j in ls :
    print(f"order is ready for {j}")


    