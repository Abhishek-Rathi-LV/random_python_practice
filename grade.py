marks=int(input("Enter The Marks = "))
if(marks>100 or 0>marks):
    print("The Marks is Invaild the Marks Should Be in range of 0-100")
elif(marks>=90):
    print("The Student Got Grade 'A'")
elif(marks>=80 and marks<90):
    print("The Student Got Grade B")
elif(marks>=70 and marks<80):
    print("The Student Got Grade c")
elif(marks>=60 and marks<70):
    print("The Student Got Grade d")
else:
    print("Student Got F Grade ")