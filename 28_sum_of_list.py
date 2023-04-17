lst = []
length = int(input("length:  "))           
for i in range(length):
    element = int(input("element")) 
    lst.append(element)
sum = 0
for a in range (len(lst)):
    sum = sum + lst[a]
print(sum)