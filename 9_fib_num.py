fib_num = int(input("num:  "))
first = 0
seconf = 1

while fib_num > 0:
    count = (fib_num - 1) + (fib_num + 2)
    fib_num = fib_num - 1
print(count)