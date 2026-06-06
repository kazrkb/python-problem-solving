a = [1,2,3]
b = [2,1,4]
a_points = 0
b_points = 0
for item in range(len(a)):
    if a[item] > b[item]:
        a_points += 1
    else:
        b_points += 1

print(a_points,b_points)
    
    