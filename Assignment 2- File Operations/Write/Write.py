#w write,create and truncate
with open("new6.txt","w") as f: #creating new file
  f.write("hello World") #Writing in File
  f.truncate() #truncate -> Size
with open("new6.txt","r") as f:
  print(f.read())

#w+ read,write,create and truncate
f2=open("new7.txt","w+") # creating new file
f2.write("Hello World") #write
print(f2.read()) # reading
lines=("\nHow \nare \nyou?")
f2.writelines(lines)
f2.seek(0)
print(f2.read())
