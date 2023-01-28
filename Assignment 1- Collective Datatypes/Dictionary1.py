# Dicitionary for Passing of Student
result={}
n=int(input("Enter Num of Stud:"))
for i in range(n):
    print("Stud no.",i+1)
    roll=int(input("Enter ROll No:"))
    name=input("Enter Name:")
    marks=int(input("Enter Marks:"))
    result[roll]=[name,marks]
print(result)
print("Passing Students")
for j in result:
    if result[j][1]>=75:
        print(result[j][0])
