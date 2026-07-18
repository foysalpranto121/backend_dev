# Linear search 
# run time complexity O(n)
# space complexity O(1)

# function

def Linear_search(arr,n,item):
    for i in range(0,n):
        if (arr[i]==item):
            return i
    return -1

## main code // driver code 
arr=[1,2,3,4,5]
n=len(arr)
item=3
index=Linear_search(arr,n,item)
if index==-1:
    print("Item not found")
else:
    print("Item found at index",index)


# Binary search 
# run time complexity O(log n)
# space complexity O(1)


# function
a = [1, 2, 3, 4, 6, 8, 12, 33, 41, 44, 100]
item = 12

left = 0
right = len(a) - 1

while left <= right:
    middle = (left + right) // 2

    if a[middle] == item:
        print("Item found at index", middle)
        break
    elif a[middle] < item:
        left = middle + 1
    else:
        right = middle - 1
else:
    print("Item not found")