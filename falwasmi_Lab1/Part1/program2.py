import random

a = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    a[i] = random.randint(0,100)
    
print(a)

num = int(input("Enter a number: "))

new_list = []

for i in range(10):
    if num > a[i]:
        new_list.append(a[i])
        
print("The new list is", new_list)