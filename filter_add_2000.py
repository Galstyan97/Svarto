def add(n):
    if n < 8000:
       return   n + 2000
    
numbers =1000, 500, 600, 700, 5000, 90000, 17500
result = map(add, numbers)
print(list(result))
