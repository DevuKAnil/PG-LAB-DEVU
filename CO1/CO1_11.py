x=int(input("enter first no:"))
y=int(input("enter second no:"))
z=int(input("enter third no:"))
if(x>y) and (x>z):largest=x
elif(y>x) and (y>z):largest=y
else:
    largest=z
    print("the largest no is",largest)
