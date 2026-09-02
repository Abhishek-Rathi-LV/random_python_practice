a=int(input("Enter the year = "))
if(a%400==0):
    print("The Year is Leap")
elif(a%4==0 and a%100!=0):
    print("The Year is Leap")
else:
    print("The Year is not a leap year ")