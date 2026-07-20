## list one dimensional=0ne row  and multiple column
product_list=['chinri mas','potol','khatal','chal','dhal']
product_price=[1000,20,300,100,150]
quantity=[1,3,3,2,3]
print(product_list[4])
print(len(product_list))
## ploymorphism=same entity different behaviour
## len is a function based on polymorphism
product_list.append('milk')
product_price.append(80)
quantity.append(2)
print(product_list)
size=len(product_list)
print(size)
for i in range(size):
    print(product_list[i],product_price[i],quantity[i],product_price[i]*quantity[i])