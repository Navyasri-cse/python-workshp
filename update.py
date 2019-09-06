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
#print(deleteitem())
def updateitem():
    d=additem(n)
    rollnum=input("enter rollnumber to update")
    name=input("enter name to update")
    branch=input("enter branch update")
    d.update({rollnum:[name,branch]})
    return d
print(updateitem())
            
