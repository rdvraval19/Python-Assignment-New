#changing the list inside tuple
t= (1, ["Hello",3], 4, 5)
print("Old Tuple=",t)
t[1][0] = "Hey"
t[1][1]=1
print("Changed tuple=",t)
#making two tuples containg odd and even no.s
t1=(1,3,4,5,6,8,5,3,46,)
print("Num Tuple=",t1)
l1=[]#for odd
l2=[]#for even
x=len(t1)
for i in range(x):
    if (t1[i])%2==0:
        l2.append(t1[i])
    else:
        l1.append(t1[i])
print("Odd Tuple TO=",tuple(l1))
print("Even Tuple TE=",tuple(l2))
    
