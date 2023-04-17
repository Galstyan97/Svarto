lst = []                                   
length = int(input("length"))
for i in range(length):
    elements = int(input("elements"))
    lst.append(elements)
smallest_num = lst[0] 
for i in lst:
    if i < smallest_num:
        smallest_num = i
print(smallest_num)           
