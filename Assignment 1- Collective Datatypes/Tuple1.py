#linear search on tuple
values=input("Enter Comma Separated Values:")
l=values.split(",")
t=tuple(l)
print(t)
print("tuple:",t)
x=input("Enter the value you want to search")
for i in range(len(t)):
    if x==t[i]:
        print("The value founded at position",i+1)
        break
else:
    print("Not founded")
