username=input("Enter the UserName")
password=input("Enter the Password")
if(username=="admin"):
    if(password=="vips123"):
        print("Login SucessFull ")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")