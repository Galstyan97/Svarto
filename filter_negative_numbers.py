def negative_numbers(n):
    if n < 0:
        return n
numbers =(1,-4,7,-9,0)   
result = filter(negative_numbers, numbers) 
print(list(result))