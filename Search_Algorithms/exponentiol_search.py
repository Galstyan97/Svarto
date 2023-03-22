def exponentialSearch(arr, n, x):
    for i in range(n):
   
        if arr[0] == x:
            return 0
         
    
        while arr[i] <= x:
        
            i = i * 2
     
    return -1

arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 3
result = exponentialSearch(arr, n, x)
if result == -1:
    print ("not found ")
else:
    print ("found")
