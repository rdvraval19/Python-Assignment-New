def a(Table,*args,**kwargs):
  print("This is a table of",Table)
  for i in args:
    for y in range(1,11):
      print(args[0],"X",y,"=",args[0]*y)
  for j in kwargs:
    print("The square of",j,"is",kwargs[j])
a("Five",5,Nine=81,Two=4,Three=9)
