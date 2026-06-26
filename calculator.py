#num1 = float(input("Enter the first number: "))
#num2 = float(input("Enter the second number: "))
#operation = input("enter your operation: ")
#if operation == "+":
  #print(num1+num2)
#elif operation == "-":
  #print(num1-num2)
#elif operation == "*":
  #print(num1*num2)
#elif operation == "/":
  #if num2 == 0:
   # print("Invalid number")
  #else:
 #   print(num1/num2)  
#elif operation == "%":
  #if num2 == 0:
 #   print("Invalid number")
 # else:
  #  print(num1/num2)
#elif operation == "**":
  #print(num1**num2)
#else:
  #print("Invalid")
result = float(input("Enter your result: "))
while True:
    operation = input("Enter your operation: ")
    if operation == "=":
        print(f"Your total result is {result}") 
        break
    elif operation == "+":
     num2 = float(input("Enter your next no.: "))
     result += num2
     print(result)
    elif operation == "*":
     num2 = float(input("Enter your next no.: "))
     result *= num2
     print(result) 
    elif operation == "-":
     num2 = float(input("Enter your next no.: "))
     result -= num2
     print(result) 
    elif operation == "%":
     num2 = float(input("Enter your next no.: "))
     if num2 == 0:
      print("invalid")
     else: 
      result %= num2
      print(result)
    elif operation == "/":
     num2 = float(input("Enter your next no.: "))
     if num2 == 0:
      print("invalid")
     else: 
      result /= num2
      print(result)
    elif operation == "**":
     num2 = float(input("Enter your next no.: "))
     result **= num2
     print(result)
    else:
      print("Invalid operation")
           
    
  