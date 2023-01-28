#Find Intersection of n sets

def intersection():
    n=int(input("Enter Num of Set you want to make"))
    y=[]
    for i in range(n):
          v=input("Enter set 1 separated with comma")
          a = v.split(",")
          y.append(set(a))
          print("Set",i+1,a)
    print("list of sets=",y)
    u = set.intersection(*y)
    print("Intersected list =",u)
intersection()

