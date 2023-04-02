
def jump_search(array, item):
    n = len(array)                          
    m = int((n))               
    i = 0                               

    while array[i] < item:

        if array[i+m-1] == item:            
            return i+m-1
        elif array[i+m-1] > item:           
        
    