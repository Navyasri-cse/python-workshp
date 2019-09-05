a=int(input("enter a value"))
i=2
while i<a:
    j=2
    while(j<=(i/j)):
        if not(i%j):break
        j+=1
    if(j>(i/j)):
            print(i,end=" ")
    i+=1
