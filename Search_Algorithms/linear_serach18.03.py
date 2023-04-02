def linear_search(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i      
    return - 1 

print(linear_search([24,78,47,75,75], 47))