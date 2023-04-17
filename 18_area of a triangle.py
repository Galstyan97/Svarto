a = float(input('Enter first num: '))          
b = float(input('Enter second num: '))  
c = float(input('Enter third num: '))  
  
s = (a + b + c) / 2  
    

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 
print(area)   