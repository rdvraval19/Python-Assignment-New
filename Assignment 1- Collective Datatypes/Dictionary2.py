#Calculating Total price 
d={}
t=0
n=int(input("Enter number of items you wish to enter"))
for i in range (n):
    n=input("Enter Name of product")
    p=int(input("Enter Price of Product"))
    q=int(input("Enter Quantity of Product"))
    d[n]=p,q
print(d)
for j in d:
    m=(d[j][1])*(d[j][0])
    t=t+m
print("Total=",t)
