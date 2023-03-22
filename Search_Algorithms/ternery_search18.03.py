# def ternary_search(array,start, end, key):
#     while start <= end:
#         mid1 = start + (end - start) /3
#         mid2 = end - (end - start) /3
#         if array[mid1] == key:
#             return mid1
#         elif array[mid2] == key:
#             return mid2
#         elif key < array[mid1]:

#             return -1
# array = [1, 2, 3, 4, 5, 6, 7]  
# start = 0
# end = 6  
# key = 3
# relult = ternary_search(array,start, end, key)
# print(relult)    

def ternarySearch(low, high, key, array):
    while high >= low:
         
        mid1 = low + (high-low) // 3
        mid2 = high - (high-low) // 3
 
        if key == array[mid1]:
            return mid1
        if key == mid2:
            return mid2
 

        if key < array[mid1]:
            high = mid1 - 1
        elif key > array[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2
 
    return -1

 
array = [10,20,30,50,70,80,100,110]
high = 9
low = 0
r = len(array) - 1
key = 250
result = ternarySearch(low, high, key, array)
print("found")