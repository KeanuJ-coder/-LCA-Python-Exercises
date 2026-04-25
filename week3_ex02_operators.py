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

# Combine the above conditions using logical operators to create a 'final_condition'
# The 'final_condition' should be True if either:
# - a is greater than b, or
# - b is even and c is less than or equal to a
a = a
b = b
c = c
final_condition = (a > b) or (b % 2 == 0 and c <= a)
print(final_condition)

