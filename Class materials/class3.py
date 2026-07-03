import math

a=float(input("Enter a : "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
d=float(input("Enter d: "))
e=float(input("Enter e: "))
ans=(((a+b)**2-(math.sqrt(d))*c)-4+((e)**2-a*c)+math.sqrt(b-1)-((a-c)*(b+2)+math.sqrt(a*a+2))/2)**3

print("The answer is: ",ans)


## today we  learn input function and math module in python.
## type casting is used to convert the input string into float data type.
## a=input("Enter a : ")  # input function is used to take input from user.
## print (type(a))  # type function is used to check the data type of variable a.
#a=int(input("Enter a : "))  # type casting is used to convert the input string into integer data type.
## good practice is solve the equation in small steps and then combine them to get the final answer.
## part 1
sub_part1=(a+b)**2
sub_part2=math.sqrt(d)*c
sub_part3=4

part1=sub_part1-sub_part2-sub_part3
##part 2
sub_part4=(e)**2-a*c
sub_part5=math.sqrt(b-1)
part2=sub_part4+sub_part5
##part 3    
sub_part6=(a-c)*(b+2)
sub_part7=math.sqrt(a*a+2)
part3=(sub_part6+sub_part7)/2
##final answer
ans=part1+part2-part3
print("The answer is: ",ans)
