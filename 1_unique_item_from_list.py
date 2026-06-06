mylist = [1,22, 5,5, 1, 22, 3, 4, 5]

unique = set(mylist)
print(unique)

#another way

unique_2 = list(dict.fromkeys(mylist))
print(unique_2)

# another way
unique_3 = []
for item in mylist:
    if item not in unique_3:
        unique_3.append(item)
print(unique_3)