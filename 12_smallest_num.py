def smallest_num(a, b,c):               
    if a == b and  a == c and b == c:
        return "is equal"
    if a <= b and a <= c:
        return a
    if b <= a and b <= c:
        return b
    if c <=a and c <=b:
        return c
    
print(smallest_num(4,4,4))   