#a write and create
with open("new8.txt","a") as f3:
  f3.write("\nMy hobby is playing Games")
f4=open("new8.txt","r")
print(f4.read())
#a+ read,write,create
with open("new9.txt","a+") as f5:#creating new file
  lines=["Hey\nHow\nare\nyou"]
  f5.writelines(lines)
  f5.write("\nOKay Bye!!")
  f5.seek(0)
  print(f5.read())
