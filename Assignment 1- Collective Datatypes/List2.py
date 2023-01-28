#TO SWAP ELEMENTS IN LIST
l=[]
t1=[]
t2=[]
sl=[]#swap list
n=int(input("Enter num of Elements (Enter Even number):"))
for i in range(n):
    ele=input("enter the element :")
    l.append(ele)
    lenth=len(l)
print("orignal list=",l)
x=len(l)
for r in range (x):
    if r%2==0:
        t1.append(l[r])
    else:
        t2.append(l[r])
print(t1)
print(t2)
y=len(t1)
for h in range(y):
    sl.append(t2[h])
    sl.append(t1[h])
print(sl)
    

