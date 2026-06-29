import random
number = random.randrange(1,101)
attempt = 1
for attempt in range(1,11):
    num = int(input("What's your guess between 1 to 100?"))
    if num == number:   
        break
    elif num > number:
        print("Too high")
    elif num < number:
        print("Too low")
won = True
if num == number:
    print(f"Congrats. That is the number, You win on attempt no. {attempt}")
else:
    print(f"you fail to guess. The number was {number}")
     