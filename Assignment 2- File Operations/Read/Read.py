#r read
with open("new.txt") as f:
  print(f.read())

#r+ read and write 
f2=open("new2.txt","r+")
f2.write("\nHello World")
print(f2.read())
lines=("\nHow \nare \nyou?")
f2.writelines(lines)
print(f2.read())
