## dictionary 
## key value pair
## key is unique
## value can be duplicate

dict1={
    "name":"pranto",
    "age":20,
    "gender":"male"
}
print(dict1)

print(dict1["name"])

print(dict1.keys())
print(dict1.values())

for i,j in dict1.items():
    print(i,j)


## update 
dict1.update({"name":"foysal"})
print(dict1)

## delete 
del dict1["name"]
print(dict1)

## clear 
dict1.clear()
print(dict1)

## copy 
dict2=dict1.copy()
print(dict2)

## nested dictionary 
dict3={
    "name":"pranto",
    "age":20,
    "gender":"male",
    "address":{
        "city":"dhaka",
        "country":"bangladesh"
    }
}
print(dict3)

## access nested dictionary 
print(dict3["address"]["city"])

## update nested dictionary 
dict3["address"]["city"]="chittagong"
print(dict3)

## delete nested dictionary 
del dict3["address"]
print(dict3)

## clear nested dictionary 
dict3.clear()
print(dict3)

## copy nested dictionary 
dict4=dict3.copy()
print(dict4)

