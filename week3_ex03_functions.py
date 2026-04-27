# Question 1: Basic Function Definition and Calling
# Define a function called 'greet' that prints "Hello, World!"
def greet():
    print('Hello,world!')
# Call the 'greet' function
greet()

# Question 2: Function with Parameters
# Define a function called 'personalized_greeting' that takes a name as a parameter and prints a personalized greeting
def personalized_greeting(name):
    print('Hello,' +name)

# Call the 'personalized_greeting' function with your name
personalized_greeting('Keanu')

# Question 3: Function with Return Value
# Define a function called 'square' that takes a number as a parameter and returns its square
# Call the 'square' function with the number 5 and print the result

number = 5
def square(result):
    return number * result
print (int(square(5)))

# Question 4: Function with Multiple Parameters and Return Value
# Define a function called 'rectangle_area' that takes length and width as parameters and returns the area of the rectangle
# Call the 'rectangle_area' function with length 4 and width 5, and print the result

length = 4
width = 5
def rectangle_area(area):
    return length * width
print(int(rectangle_area(5)))

# Question 5: Using a Function as an Argument
# Define a function called 'apply_operation' that takes a function and a number as parameters, and returns the result of applying the function to the number
# Define a function called 'double' that takes a number as a parameter and returns its double
# Use the 'apply_operation' function with the 'double' function and the number 7, and print the result
# Use the 'apply_operation' function with the 'square' function (defined in Question 3) and the number 3, and print the result

def apply_operation(function,number):
    return function(number)
#Function to a double a number 
def double(number):
    return number * 2
result_double = apply_operation(double,7)
print(f"double result:{result_double}")
#Function to square a number (from question 3)
def square(number):
    return number **2
result_square = apply_operation(square,3)
print(f"square result: {result_square}")