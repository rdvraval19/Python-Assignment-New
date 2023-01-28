l=[]
n=int(input("Enter Num of Elements to enter:"))
for i in range(n):
    x=input("Do you want to enter integer\nYes or No :")
    if x=="Yes":
        ele=int(input("Enter Element:"))
        l.append(ele)
    else:
        ele=input("Enter Element:")
        l.append(ele)
print(l)
