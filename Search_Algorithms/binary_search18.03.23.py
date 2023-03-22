def binary_search(array, x, low, high): 
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
        
    return - 1

array = [2,4,7,8,9,10]
x = 9
low = 0
high = len(array) - 1
result = binary_search(array, x, low, high)
if result == -1:
    print("not found")
else:
    print("found")    