tup=(1,4,9,16,25,49,64,81,100)
x=int(input("Enter the Number you want to search "))
c=0
for elements in tup:

    if elements==x:
        print("Element is present in the list  at index", c)
        break
    c+=1
else:
    print("Element not in the tuple")
    