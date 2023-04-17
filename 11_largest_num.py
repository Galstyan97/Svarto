def largest_num(a, b, c,):
    if a == b and a == c and b ==c:
        return "it is equal"
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    if c >= a and c >= b:
        return c
print(largest_num(4,4,2))    
