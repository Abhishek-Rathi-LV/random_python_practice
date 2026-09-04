N=int(input("Enter the Value of N"))
for i in range (2,N+1,1):
    is_prime=True
    for j in range (2,i,1):
        if i %j==0:
            is_prime=False
            break
    if is_prime:
        print(i)
