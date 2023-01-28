#Finding Max and Min element of a Set
import math
v=input("Enter Comma Separated Values:")
l=v.split(",")
s=set(l)
print(s)
print("Maximum Value=",max(s))
print("Minimum Value=",min(s))
