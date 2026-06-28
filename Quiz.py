score = 0
Q1 = input("Enter the capital of India: ")
if Q1.lower() == "delhi":
    score += 10
    print("Correct")
else:
    print("Wrong!Correct answer is Delhi")
Q2 = input("Enter he capital of US: ")
if Q2.lower() == "washington":
    score += 10
    print("Correct")
else:
    print("Wrong!Correct answer is Washington")
Q3 = input("Enter he capital of UK: ")
if Q3.lower() == "london":
    score += 10
    print("Correct")
else:
    print("Wrong!Correct answer is London")
Q4 = input("Enter he capital of France: ")
if Q4.lower() == "paris":
    score += 10
    print("Correct")
else:
    print("Wrong!Correct answer is Paris")
Q5 = input("Enter he capital of Japan: ")
if Q5.lower() == "tokyo":
    score += 10
    print("Correct")
else:
    print("Wrong!Correct answer is Tokyo")
grade = score
if score == 50:
    print("Grade = A")
elif score == 40:
    print("Grade = B")
elif score == 30:
    print("Grade = C")
elif score < 30:
    print("Grade = D")
print(f"Your score is {score}")