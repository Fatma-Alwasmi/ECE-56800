count = int(input("How many Fibonacci numbers would you like to generate? "))

a = 0
b = 1
c = a

while count != 0:
    print(c, ",", end= " ")
    count -=1
    a, b = b, c
    c = a + b

            
    
        
    
     
    