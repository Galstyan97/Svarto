def vowel(n):
    if n in "AaOoUuIiEe":
        return n
string = "Hello my world"
result = filter(vowel,string)
print(list(filter(vowel, string)))