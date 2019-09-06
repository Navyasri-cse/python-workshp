def additem(n):
        d={}
        for i in range(n):
            rollnum=input("enter rollnumber")
            name=input("enter name")
            branch=input("enter branch")
            d[rollnum]=[name,branch]
        return d
n=int(input("enter a value"))
def deleteitem():
    d=additem(n)
    k=input("enter the rolnum to deleted")
    d.pop(k)
    return d
print(deleteitem())
