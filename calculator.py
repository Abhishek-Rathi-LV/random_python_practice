a=float(input("Enter the First Number :- "))
b=float(input("Enter the second Number :- "))
o=input("Enter operator (+ - * /):")
if o=="+":
    print(a,"+",b,"=",a+b)
elif o=="-":
    print(a,"-",b,"=",a-b)
elif o=="*":
    print(a,"*",b,"=",a*b)
elif o=="/":
    if b!=0:
       print(a,"/",b,"=",a/b)
    else:
        print("Divison by zero not possible")
else:
    print("Invalid Opreator Selected")