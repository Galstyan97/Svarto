def even_num(n):
    if n % 2 == 1:
        return n
numbers = (2,3,15,45,23)
result = filter(even_num, numbers)    
print(list(result))