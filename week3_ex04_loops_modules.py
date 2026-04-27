# Question 1: Using a for loop with a list
# Create a list of fruits
fruits=["banana","blueburry","cherry","apple"]
# Use a for loop to print each fruit in the list
for fruit in fruits:
    print(fruit)

# Question 2: Using a while loop for countdown
# Use a while loop to create a countdown from 5 to 1
count = 5
while count >= 1:
    print(count)
    count -= 1

# Question 3: Using a for loop with range()
# Use a for loop to print the first 10 square numbers
for i in range(1, 11):
    square = i ** 2
    print(f"the square if {i} is {square}")

# Question 4: Using the random module
# Import the random module
import random 
# Create a list of colours
colors = ["red","blue","green","yellow","cyan","orange","purple"]
# Use a for loop to select and print 3 random colors from the list 
for i in range (3):
    random_color = random.choice(colors)
    print(f'random selection {i+1}: {random_color}')

# Question 5: Creating and using a custom module
# Create a new file named 'math_operations.py' with the following content:

# Import the custom module and use its functions
import math_operations as mo 
# Use a while loop to create a simple calculator
print("---simple python calculator ---")
print("enter 'quit' to exit.")
while True:
    operation = input("\nchoose operation (+,-,*,/) or 'quit':").lower()
    if operation == 'quit':
        print("Goodbye!")
        break
    if operation in ['+','-','*','/']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if operation =='+':
                print(f"result: {mo.add(num1, num2)}")
            elif operation == '-':
                print(f"result: {mo.subtract(num1, num2)}")
            elif operation == '*':
                print(f"result: {mo.multiply(num1, num2)}")
            elif operation == '/':
                print(f"result: {mo.divide(num1, num2)}")
        except ValueError:
            print("Invaild input! Please enter numeric values.")
    else:
        print("Invalid operation. Please try again.")



