lst = []                                    
length = int(input("length"))
for i in range(length):
    elements = int(input("elements"))
    lst.append(elements)
largest_num = lst[0]
for a in lst:
    if a > largest_num:
        largest_num = a
print(largest_num)       