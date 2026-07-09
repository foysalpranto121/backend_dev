import math

n = int(input())   

centers = []
for i in range(n):
    line = input().split()   
    centers.append(line)   


point = input().split()
px = int(point[0])
py = int(point[1])


answer = ""
min_dist = 999999999   

for c in centers:
    name = c[0]
    x = int(c[1])
    y = int(c[2])

    d = math.sqrt((x - px)**2 + (y - py)**2)   

    if d < min_dist:    
        min_dist = d    
        answer = name    

print(answer)