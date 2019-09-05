a=int(input("enter a value"))
b=int(input("enter b value"))
print("1.add 2.sub 3.mul 4.div 5.mod ")
ch=int(input("enter your choice"))
if ch==1:
    print("addition:",a+b)
elif ch==2:
    print("subtraction:",a-b)
elif ch==3:
    print("product:",a*b)
elif ch==4:
    print("division:",a/b)
elif ch==5:
    print("modulus:",a%b)
else:
    print("invalid")
