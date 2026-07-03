import math

a=float(input("Enter a : "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
d=float(input("Enter d: "))
e=float(input("Enter e: "))
ans=(((a+b)**2-(math.sqrt(d))*c)-4+((e)**2-a*c)+math.sqrt(b-1)-((a-c)*(b+2)+math.sqrt(a*a+2))/2)**3
print("The answer is: ",ans)
