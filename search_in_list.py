l=[10,20,30,30,50,60,70,80]
x=int(input("Enter the Number-:"))
f=0
n=len(l)-1
idx=0
while idx<=n:
    if l[idx]==x :
        f+=1
        break
    idx+=1
if f :
    print("Number is available at index ",idx,"in the list")
else:
    print("Not in the list")
