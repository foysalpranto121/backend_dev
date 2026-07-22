##function 

def add(a,b):
    return a+b

print(add(2,3))

## lambda function 
add=lambda a,b:a+b
print(add(2,3))

## map function 
list1=[1,2,3,4,5]
list2=[2,3,4,5,6]
list3=list(map(add,list1,list2))
print(list3)

## filter function 
list1=[1,2,3,4,5]
list2=list(filter(lambda a:a%2==0,list1))
print(list2)

## reduce function 
from functools import reduce
list1=[1,2,3,4,5]
list2=reduce(add,list1)
print(list2)