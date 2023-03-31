def factorial(n):
    if n < 0:   
        print("error")
        return 
             
    fac = 1
    while n > 0:
        if n == 1:
            yield fac
        else: 
            fac = n * fac
        n = n - 1
    

call = factorial(5)
print(next(call))
