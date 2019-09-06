l=list(map(int,input("enter list of elements:").split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(sorted(l1))

