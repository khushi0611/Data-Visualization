
# 1. Using input() function take one number from the user and using ternary operators
# check whether the number is even or odd
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number {number} is {result}.")

# 2. Using input function take two numbers and then swap the numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")

# 3. Write a Program to Convert Kilometers to Miles
kilometers = float(input("Enter the distance in kilometers: "))
miles = kilometers * 0.621371
print(f"{kilometers} kilometers is equal to {miles} miles.")

# 4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year
principal = 200
rate = 5
time = 5
simple_interest = (principal * rate * time) / 100
print(f"The simple interest on Rs. 200 for 5 years at 5% per year is Rs. {simple_interest}.")
