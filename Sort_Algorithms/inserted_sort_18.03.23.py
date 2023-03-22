def inserted_sort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1     
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array    


data = [9, 5, 1, 4, 3]
print(inserted_sort([2,7,5,1,4,3]))
