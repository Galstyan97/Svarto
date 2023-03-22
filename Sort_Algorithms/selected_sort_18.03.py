def selected_sort(array):
    n = len(array)
    for i in range(n):
        min_num = i
        for j in range(i, n):
            if array[min_num] >  array[j]:
                min_num = j
        array[i], array[min_num] = array[min_num], array[i]
    return array


print(selected_sort([4,7,2,1,5]))