lst = []                                 
length = int(input("length num"))
for a in range(length):
    element = int(input("element"))
    lst.append(element)
lst = lst[::-1]
print(lst)   