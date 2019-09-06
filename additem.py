def additem(n):
    d={}
    for i in range(n):
        rollnum=input("enter rollnumber")
        name=input("enter name")
        branch=input("enter branch")
        d[rollnum]=[name,branch]
    return d
n=int(input("enter a value"))
print(additem(n))
