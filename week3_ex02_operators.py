# Question 1: Arithmetic and Assignment Operators
# Add 3 to x using the += operator
x=3
# Multiply y by 2 using the *= operator
y=2 
y = y*2
# Divide x by y and store the result in a variable called 'result'
result = x/y
print(x)
#Print the value of 'result'
result=0.75
print(result)
# Question 2: Comparison and Logical Operators
#: Create a condition that checks if a is greater than b
a='a'
b='b'
print(a>b)
# Create a condition that checks if b is even (hint: use the modulus operator)
b = 4
if b % 2 == 0:
  print('b is even')
else:
  print('b is odd')
#I've been struggling with this qustion. To make it even it but this is the formula i used.

#Create a condition that checks if c is less than or equal to a
x = a
y = 'c'
if x > y:
  print("x is greater than y")
elif x == y:
  print("x is equal to y")
else:
  print("x is less than or equal to y")

#Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b
#       - b is even and c is less than or equal to a
a='a'
b=b 
c='c'
if 'a' > 'b':
  print('a is greater than b')
elif b % 2 == 0:
  print('b is even')
else:
  print('c is less than or equal to a')

#Print the value of 'final_condition'
finalcondition =('a>b')and('a<c')
print(finalcondition)

# Question 3: Conditional Statements
# Ask the user to input a test score (0-100) and store it in a variable called 'score'
#('test score') = (0-100)
score = 0-100
# Implement a grading system using if-elif-else statements:
#       90-100: A
if score >= 90:
  grade = "a"
#       80-89: B
elif score >= 80:
  grade ='b'
#       70-79: C
elif score >= 70:
  grade ='c'
#       60-69: D
elif score >= 60:
  grade ='d'
#       Below 60: F
else:
  grade = 'f'
#Print the grade for the given score
print(f'for a score of {score}, the grade is: {grade}')

# Question 4: Combining Operators and Conditionals
# Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = 5
num2 = 10
# Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Operation(+,-,*,/):")
print(f"you selected the '{operation}' operation")
# Use conditional statements to perform the chosen operation on num1 and num2
if operation =="+":
  result = num1 + num2
elif operation =="-":
  result = num1 - num2 
elif operation == "*":
  result = num1 * num2
elif operation == "/":
  result = num1 / num2 
else:
  result = "invaild operation"
  print(f"result: {result}")
  