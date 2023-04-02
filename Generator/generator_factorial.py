def fibonacii(n):
    x, y = 0, 1
    while x < n:
        yield x
        x, y = y, x + y
# call = fibonacii(10)
# print(next(call))
# print(next(call))
# print(next(call))
# print(next(call))
for i in fibonacii(10):
    print(i)