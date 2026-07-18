## class task 

## liner search
contact_list = ['salman','nahid','sujon','Latifa','siyam','shuvo','rashed','durjoy','fahim','tanvir','anik','imaran','jahedul','salman','shuvo','durjoy','nahid']

target = input("give your target: ")

size_contact = len(contact_list)
print(f"size {size_contact}")
result = -1
result_list = []
# contact_list = ['salman','nahid','sujon','Latifa','siyam','shuvo','rashed','durjoy','fahim','tanvir','anik','imaran','jahedul','salman','shuvo','durjoy','nahid']
for i in range(size_contact):
    print(contact_list[i])
    print(i)
    if(target==contact_list[i]):
        result  = i
        result_list.append(i)
        print(result_list)



if result == -1:
    print("not found")
else:
    print(f"the {target} is found at index {result_list}")
#formatted, break in foor loop

## solving my way  using function 

def contact_search(contact_list,target,size_contact):
    for i in range(0,size_contact):
        if(contact_list[i]==target):
            return i
    return -1


contact_list = ['salman','nahid','sujon','Latifa','siyam','shuvo','rashed','durjoy','fahim','tanvir','anik','imaran','jahedul','salman','shuvo','durjoy','nahid']

target = input("give your target: ")
size_contact=len(contact_list)
result=contact_search(contact_list,target,size_contact)
if result==-1:
    print("not found")
else:
    print(f"the {target} is found at index {result}")