import random

# 1. Declare a div() function with two parameters. Then call the function and pass two
# numbers and display their division.
def div(a, b):
    return a / b



# Call the function and pass two numbers
result = div(10, 2)
print(f"Division result: {result}")



# 2. Declare a square() function with one parameter. Then call the function and pass
# one number and display the square of that number.
def square(num):
    return num * num

# Call the function and pass one number
result = square(5)
print(f"Square result: {result}")



# 3. Using max() and min() functions display the maximum and minimum of 5 random
# numbers.
numbers = [random.randint(1, 100) for _ in range(5)]
print(f"Random numbers: {numbers}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")



# 4. Accept a name from the user and display that in lower case using lower() function.
name = input("Enter your name: ")
print(f"Name in lower case: {name.lower()}")




# Assignment:
# 1. Write a Python program to count the occurrences of each word in a given sentence.
# string = “To change the overall look of your document. To change the look available in the gallery”
sentence = "To change the overall look of your document. To change the look available in the gallery"
words = sentence.split()
word_count = {}
for word in words:
    word = word.strip('.').lower()
    word_count[word] = word_count.get(word, 0) + 1
print("Word occurrences:", word_count)



# 2. Write a Python program to remove a newline in Python
# String = "\nBest \nDeeptech \nPython \nTraining\n"
string_with_newlines = "\nBest \nDeeptech \nPython \nTraining\n"
string_without_newlines = string_with_newlines.replace('\n', '')
print("String without newlines:", string_without_newlines)



# 3. Write a Python program to reverse words in a string
# String = “Deeptech Python Training”
string_to_reverse = "Deeptech Python Training"
reversed_string = ' '.join(string_to_reverse.split()[::-1])
print("Reversed string:", reversed_string)



# 4. Write a Python program to count and display the vowels of a given text
# String=”Welcome to python Training”
string = "Welcome to python Training"
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in string if char in vowels)
print(f"Total vowels in the string: {vowel_count}")




# Assignment:
# 1. Write a Python program to count all letters, digits, and special symbols from the given string
# Input = “P@#yn26at^&i5ve”
# Output: Chars = 8 Digits = 2 Symbol = 3
input_string = "P@#yn26at^&i5ve"
chars = sum(c.isalpha() for c in input_string)
digits = sum(c.isdigit() for c in input_string)
symbols = sum(not c.isalnum() for c in input_string)
print(f"Chars = {chars} Digits = {digits} Symbols = {symbols}")



# 2. Write a Python program to remove duplicate characters of a given string.
# Input = “String and String Function”
# Output: String and Function
input_string = "String and String Function"
output_string = ""
seen = set()
for char in input_string:
    if char not in seen:
        seen.add(char)
        output_string += char
print("String without duplicates:", output_string)



# 3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
# Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
# Output:
# UpperCase : 5
# LowerCase : 18
# NumberCase : 5
# SpecialCase : 11
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase_count = sum(c.isupper() for c in input_string)
lowercase_count = sum(c.islower() for c in input_string)
numeric_count = sum(c.isdigit() for c in input_string)
special_count = sum(not c.isalnum() for c in input_string)
print(f"UpperCase : {uppercase_count}")
print(f"LowerCase : {lowercase_count}")
print(f"NumberCase : {numeric_count}")
print(f"SpecialCase : {special_count}")



# 4. Write a Python program to count vowels in a string
# input = “Welcome to Python Assignment”
# Output: Total vowels are: 8
input_string = "Welcome to Python Assignment"
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in input_string if char in vowels)
print(f"Total vowels in the string: {vowel_count}")
