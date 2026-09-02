a=float(input("Enter the first Number = " ))
b=float(input("Enter the Second Number = " ))
c=input("Enter the opreater (+,-,/,* only)")
if(c=="+"):
    res=a+b
    print("The Addtion of Both Number are ",res)
elif(c=="-"):
    res=a-b
    print("The Subtraction of Both Number are ",res)
elif(c=="*"):
    res=a*b
    print("The Multipliaction of Both Number are ",res)
elif(c=="/"):
    if(b!=0):
     res=a/b
     print("The division of Both Number are ",res)
    else:
       print("Division By Zero is Not aloowed")
else:
   print("Invalid Opreator")