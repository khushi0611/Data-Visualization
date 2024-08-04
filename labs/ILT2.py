# 1. Python program to check leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



# 2. Python Program to Find the Largest Among Three Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
largest = max(num1, num2, num3)
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")



# 3. Python Program to Check if a Number is Positive, Negative or 0
number = float(input("Enter a number: "))
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")



# 4. A toy vendor supplies three types of toys: Battery Based Toys, Key-based
# Toys, and Electrical Charging Based Toys. The vendor gives a discount of
# 10% on orders for battery-based toys if the order is for more than Rs. 1000.
# On orders of more than Rs. 100 for key-based toys, a discount of 5% is
# given, and a discount of 10% is given on orders for electrical charging based
# toys of value more than Rs. 500. Assume that the numeric codes 1, 2 and 3
# are used for battery based toys, key-based toys, and electrical charging based
# toys respectively. Write a program that reads the product code and the order
# amount and prints out the net amount that the customer is required to pay
# after the discount.
product_code = int(input("Enter product code (1 for Battery Based Toys, 2 for Key-based Toys, 3 for Electrical Charging Based Toys): "))
order_amount = float(input("Enter order amount: "))
if product_code == 1 and order_amount > 1000:
    discount = order_amount * 0.10
elif product_code == 2 and order_amount > 100:
    discount = order_amount * 0.05
elif product_code == 3 and order_amount > 500:
    discount = order_amount * 0.10
else:
    discount = 0
net_amount = order_amount - discount
print(f"The net amount to be paid is Rs. {net_amount}.")



# 5. A transport company charges the fare according to following table:
# Distance Charges
# 1-50 8 Rs./Km
# 51-100 10 Rs./Km
# > 100 12 Rs/Km
distance = float(input("Enter the distance in km: "))
if 1 <= distance <= 50:
    fare = distance * 8
elif 51 <= distance <= 100:
    fare = 50 * 8 + (distance - 50) * 10
else:
    fare = 50 * 8 + 50 * 10 + (distance - 100) * 12
print(f"The fare for {distance} km is Rs. {fare}.")



# 6. Write a python program to reverse a number using a while loop.
number = int(input("Enter a number to reverse: "))
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
print(f"Reversed number is {reversed_number}.")



# 7. Write a python program to check whether a number is palindrome or not.
number = int(input("Enter a number: "))
original_number = number
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")



# 8. Write a python program finding the factorial of a given number using a while loop.
number = int(input("Enter a number to find its factorial: "))
factorial = 1
temp = number
while temp > 0:
    factorial *= temp
    temp -= 1
print(f"The factorial of {number} is {factorial}.")



# 9. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.
sum_of_numbers = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    sum_of_numbers += number
print(f"The sum of all numbers entered is {sum_of_numbers}.")



# 10. Print the first 10 natural numbers using for loop.
for i in range(1, 11):
    print(i, end=' ')
print()



# 11. Python program to check if the given string is a palindrome.
string = input("Enter a string: ")
if string == string[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")



# 12. Python program to check if a given number is an Armstrong number.
number = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) ** len(str(number)) for digit in str(number))
if number == sum_of_digits:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")



# 13. Python program to get the Fibonacci series between 0 to 50.
a, b = 0, 1
print("Fibonacci series between 0 to 50: ")
while a <= 50:
    print(a, end=' ')
    a, b = b, a + b
print()

# 14. Python program to check the validity of password input by users.
def is_valid_password(password):
    if len(password) < 8:
        return False
    
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special_char = False
    special_chars = "@#$%^&+="
    
    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True

    return has_lowercase and has_uppercase and has_digit and has_special_char

password = input("Enter a password: ")
if is_valid_password(password):
    print("Valid password.")
else:
    print("Invalid password.")
