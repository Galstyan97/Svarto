def sentinelSearch(array, n, key):
    last = array[n - 1]
    array[n - 1] = key
    i = 0
    while (array[i] != key):
        i = i + 1
    array[n - 1] = last
    if ((i < n - 1) or (array[n - 1] == key)):
        print("found")
    else:
        print("Not found")
 
array = [5, 24, 10, 7, 24, 2, 15, 8, 12]
n = len(array)
key = 88
 
sentinelSearch(array, n, key)
