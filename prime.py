a=int(input("enter a number"))
i=1
j=0
while i<=a:
    if a%i==0:
        j+=1
    i+=1
if j==2:
    print("prime")
else:
    print("not prime")
