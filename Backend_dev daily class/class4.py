## list  class 4
list1=["kasem","hasem","rahim","jhon","ahmed"]
print(list1)
## list changeabke--->> 
# 1- add
# 2-remove 
# 3- duplicate allowed 


list2=["kasem","hasem","rahim","jhon","ahmed","kasem"]
print(list2) ## allowed duplicated 
## len() func 
print(len(list2))

print(type(list2))

## index 
print(list2[2])
print(list2[-1])
print(list2[2:4])
print(list2[:4])
print(list2[2:])

## change items 
list2[2]="pranto"
print(list2) 

## python add list 
list2.append("foysal")
print(list2)

## python insert list 
list2.insert(2,"ahmed")
print(list2)

## extend list 
list3=["pranto","foysal"]
list2.extend(list3)
print(list2)

## python remove list 
list2.remove("foysal")
print(list2)

## python pop list 
list2.pop(2)
print(list2)

## python clear list 
list2.clear()
print(list2)

## del list 
del list2[2]
print(list2)
## rever set list 
list2.reverse()
print(list2)

## sort list 
list2.sort()
print(list2)

## copy list 
list4=list2.copy()
print(list4)
