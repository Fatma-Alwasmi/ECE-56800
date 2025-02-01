import random

num = random.randint(0, 10)


guess = int(input("Enter your guess:"))

for i in range(2):
    if guess == num:
        print("You win!")
        break
    else:
        guess = int(input("Enter your guess:"))
        
print("You lose!")        