unit=float(input("Enter the Electricity Consumption In Unit"))
if(unit<0):
    print("Invalid Units ")
elif(unit<=100):
    print("The Rate Will be apllied is Rs 5 per Unit" )
    print("You Have to pay = ",unit*5)
elif(unit<=200):
    print("The Rate Will be apllied is Rs 7 per Unit" )
    print("You Have to pay = ",unit*7)
else:
    print("The Rate Will be apllied is Rs 10 per Unit" )
    print("You Have to pay = ",unit*10)
