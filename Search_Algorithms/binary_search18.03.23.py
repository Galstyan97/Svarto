def binary_search(array, searching_element, low, high): 
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == searching_element:
            return mid
        elif array[mid] < searching_element:
            low = mid + 1
        else:
            high = mid - 1
        
    return - 1

array = [2,4,7,8,9,10]
searching_element = 9
low = 0
high = len(array) - 1
result = binary_search(array, searching_element, low, high)
if result == -1:
    print("not found")
else:
    print("found")    
