def positive_integers(str = "Anahit2 47Gad8cf4"):
    for i in str:
        if ord(i) >  48 and ord(i) < 58:
            return i 
str = "djf78fnjv 78dfk 7diodjfk17"   
result = filter(positive_integers, str)
print(list(result))

