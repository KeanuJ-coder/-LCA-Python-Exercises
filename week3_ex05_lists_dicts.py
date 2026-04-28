# Question 1: Creating and Modifying Lists
# Create a list of fruits
fruits = ["apple","banana","cherry"]
# Add a fruit to the end of the list 
fruits.append("orange")
# Insert a fruit at the beginning of the list 
fruits.insert(0, "strawberry")
# Remove a fruit from the list 
fruits.remove("banana")
# Print the modified list 
print(fruits)

# Question 2: List Operations
# Create a list of numbers from 1 to 5
numbers = [1,2,3,4,5]
# Create a new list with each number squared
# Using list comprehension: [expression for item in list]
squared_numbers = [n**2 for n in numbers]
# Find the sum and average of the original numbers
total_sum = sum(numbers)
average = total_sum / len(numbers)
# Print the results
print(f"Original Numbers: {numbers}")
print(f"Squared Numbers: {squared_numbers}")
print(f"sum: {total_sum}")
print(f"Average: {average}")

# Question 3: Creating and Modifying Dictionaries
# Create a dictionary of countries and their capitals
capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}
# Add a new country-capital pair 
capitals["Germany"] = "Berlin"
# Updates the capital of an existing country
capitals["USA"] = "Washington, D.C."
# Remove a country-capital pair 
del capitals["France"]
# Print the modified dictionary 
print(capitals)

# Question 4: Dictionary Operations
# Create a dictionary of fruit colors
fruit_colors = {
    "apple":"red",
    "banana":"yellow",
    "blueberry":"blue",
    "kiwi": "green"
}

# Print all the fruits (keys)
print("fruits:", list(fruit_colors.keys()))
# Print all the colors (values)
print("colors:", list(fruit_colors.values()))

# Print each fruit and its color
print("\nFruit Inventory:")
for fruit,color in fruit_colors.items():
    print(f"The {fruit} is {color}.")

# Check if a fruit is in the dictionary and print its color
search_fruit = 'apple'
if search_fruit in fruit_colors:
    print(f"\nYes, we have {search_fruit}! its color is {fruit_colors[search_fruit]}.")
else:
    print(f"\nSorry, {search_fruit} is not in the dictionary.")
