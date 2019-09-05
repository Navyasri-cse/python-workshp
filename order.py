a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
if a>b and a>c:
    print("first:",a)
    if b>c:
        print("second:",b)
        print("third:",c)
    else:
        print("second:",c)
        print("third:",b)
elif b>a and b>c:
    print("first:",b)
    if a>c:
        print("second:",a)
        print("third:",c)
    else:
        print("second:",c)
        print("third:",a)
else:
    print("first:",c)
    if a>b:
        print("second:",a)
        print("third:",b)
    else:
        print("second:",b)
        print("third:",a)
        
