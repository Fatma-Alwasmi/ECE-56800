count = int(input("How many Fibonacci numbers would you like to generate? "))

a = 0
b = 1
c = a


fib = []

while count > 0:
    fib.append(c)
    count -=1
    a, b = b, c
    c = a + b

x = ", ".join(map(str, fib))
print("The Fibonacci Sequence is: " + x )       
