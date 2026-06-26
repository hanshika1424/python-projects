import random
your_result = 0
computer_result = 0
for round in range(5):
  choice = input("Enter your choice (rock, paper, scissor): ").lower()
  options = ["rock", "paper", "scissor"]
  random_choice = random.choice(options)
  print(f"you choice is {choice} and computer choice is {random_choice}")
  
  if choice == random_choice:
    print(f"your score is {your_result}")
    print(f"computer score is {computer_result}")

  elif choice == "rock" and random_choice == "scissor":
    your_result += 10
    print(f"your score is {your_result}")
    print(f"computer score is {computer_result}")
    
  elif choice == "rock" and random_choice == "paper":
    computer_result += 10
    print(f"your score is {your_result}")
    print(f"computer score is {computer_result}")
   

  elif choice == "scissor" and random_choice == "paper":
    your_result += 10
    print(f"your score is {your_result}")
    print(f"computer score is {computer_result}")

  elif choice == "scissor" and random_choice == "rock":
    computer_result += 10
    print(f"your score is {your_result}")
    print(f"computer score is {computer_result}")

  elif choice == "paper" and random_choice == "scissor":
    computer_result += 10
    print(f"your score is {your_result}")
    print(f"computer score is {computer_result}")

  elif choice == "paper" and random_choice == "rock":
    your_result += 10
    print(f"your score is {your_result}")
    print(f"computer score is {computer_result}")

  else:
    print("invalid")
    break

if your_result > computer_result:
 print(f"YOUR FINAL SCORE is {your_result}")
 print(f"COMPUTER'S FINAL SCORE is {computer_result}")
 print("YOU WIN!")
elif your_result < computer_result:
 print(f"YOUR FINAL SCORE is {your_result}")
 print(f"COMPUTER FFINAL SCORE is {computer_result}")
 print("COMPUTER WIN!")
elif your_result == computer_result: 
 print(f"YOUR FINAL SCORE is {your_result}")
 print(f"COMPUTER FINAL SCORE is {computer_result}")
 print("IT IS A DRAW!")
