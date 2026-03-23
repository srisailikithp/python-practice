# Q.1.Write a program to store seven fruits in a list enterd by the user.
A = []
f1 = input("enter fruit value")
A.append(f1)
f2 = input("enter fruit value")
A.append(f2)
f3 = input("enter fruit value")
A.append(f3)
f4 = input("enter fruit value")
A.append(f4)
f5 = input("enter fruit value")
A.append(f5)
f6 = input("enter fruit value")
A.append(f6)
f7 = input("enter fruit value")
A.append(f7)
print("fruits list =",A)

# Q2.Write a program to accept maks of six students and display them in a sorted manner .
A = []

f1 = input("enter marks")
A.append(f1)
f2 = input("enter marks")
A.append(f2)
f3 = input("enter marks")
A.append(f3)
f4 = input("enter marks")
A.append(f4)
f5 = input("enter marks")
A.append(f5)
f6 = input("enter marks")
A.append(f6)

A.sort()

print("the marks of six students are" , A)

# Q3.Type a program to sum a list with 4 numbers . 
L = [3,3,4,8]

print(sum(L))

# Q4.Write a program to count the number of zeros in following tuple :
a = (7,0,0,0,3,4,0,4)
print(a.count(0))
