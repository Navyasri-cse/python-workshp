list1=[10,20,30,40]
list2=[50,60,70,80]
k=len(list1)
l=[]
if len(list2)==k:
    for i in range(k):
        t=list1[i]+list2[i]
        l.append(t)
    print(l)
else:
    print("addition not possible")
