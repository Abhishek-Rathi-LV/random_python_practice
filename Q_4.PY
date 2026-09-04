a=int(input("Enter the First Number "))
b=int(input("Enter the Second Number "))
c=int(input("Enter the third Number "))

if(a==b and a==c):
    print("All the numbers are equal ")
elif(a==b and a>c):
    print("A and B are eaual and Greatest")
elif(a==c and a>b):
    print("A and c are eaual and Greatest")
elif(b==c and b>a):
    print(" B and C are the greatest")
elif(a>b and a>c):
    print("A is The Biggest")
elif(b>a and b>c):
    print("B is the biggest ")
else:
    print("C is the greatest ")
