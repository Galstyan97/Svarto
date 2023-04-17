lst = []                                     
length = int(input("length"))
for i in range(length):
    elements = int(input("elements"))
    lst.append(elements)
product = 1
for a in range(len(lst)):
    product =product * lst[a]
print(product)    
