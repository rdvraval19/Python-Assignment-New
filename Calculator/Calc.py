i=0
while(i==0):
  a=int(input("Enter Num1:"))
  b=int(input("Enter Num2:"))
  c=int(input("1.Multiplication\n2.Addition\n3.Subtraction\n4.Division\nEnter your choice:"))
  if c==1:
    print(a,"*",b,"=",a*b)
  elif c==2:
    print(a,"+",b,"=",a+b)
  elif c==3:
    print(a,"-",b,"=",a-b)
  elif c==4:
    print(a,"/",b,"=",a/b)
  else:
    print("Wrong Input")
