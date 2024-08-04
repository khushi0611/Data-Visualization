# Assignment:
# 1. write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.
lines=['Ensures safe file handling with automatic closure using with.\n','Handles exceptions gracefully for missing files or other errors.\n','Processes and prints each line without extra newline characters.']
with open('ABC.txt','w') as file:
  file.writelines(lines)

def read_file_line_by_line (filename):
  try:
    with open ('ABC.txt','r') as file:
      for line in file:
        print(line.strip())
  except FileNotFoundError:
    print('File name "ABC.txt" does not exist')

read_file_line_by_line('ABC.txt')



# 2. write a function in python to count and display the tatal number of words in a text file "ABC.txt"
with open('ABC.txt','r') as file:
  content = file.read()
  words = content.split()
print(content)
print(words)
print(len(words))



# 3.write a function in python to count uppercase character in a text file "ABC.txt"
count=0
with open('ABC.txt','r') as file:
  content = file.read()
  for char in content:
    if char.isupper():
      count=count+1
print(count)




text = """This is a sample text designed to be used for testing file reading in Python.
Each line in this text file will be separated by a newline character.
The purpose of this text is to demonstrate how to read and process lines from a file.
This ensures that you can test reading files where each line might contain different content.
You can use this text to validate that your file reading and processing code works correctly.
Each line is kept short to ensure that the example remains clear and easy to understand.
Make sure to save this text in a file and use it to test various file handling techniques.
This will help in understanding how files are read line by line in Python.
By following these instructions, you can practice file I/O operations efficiently.
This is the end of the sample text meant for demonstration purposes."""
# Write the text to a file
with open('story.txt', 'w') as file:
    file.write(text)

# 4.write a function display_words in python to read lines from a text file "story.txt" and display those wprds which are less than 4 characters.
def display_words(max_char):
 with open('story.txt','r') as file:
   content = file.read()
   words = content.split()
   for string in words:
     if len(string)<max_char:
       print(string,end=',')
display_words(4)



#Assignment
# 1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try :
    x=int(input("enter x "))
    y=int(input("enter y "))
    z=x/y
    print(f"x/y = {z}")

except ZeroDivisionError as e:
    print(e)


# 2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try :
    x=int(input("enter x "))
    print(x)
except ValueError as e:
    print(e)


# 3.Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

# lines=['Ensures safe file handling with automatic closure using with.\n','Handles exceptions gracefully for missing files or other errors.\n','Processes and prints each line without extra newline characters.']
# with open('ABC.txt','w') as file:
#   file.writelines(lines)
try:
    with open ('ABC.txt','r') as file:
      for line in file:
        print(line.strip())
except FileNotFoundError as e:
    print(e)


# 4.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical
def get_number_input(prompt):
    user_input = input(prompt)
    try:
        return float(user_input)
    except ValueError:
        raise TypeError(f"Invalid input: '{user_input}' is not a numerical value.")

try:
    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")
    print(f"The numbers you entered are {num1} and {num2}.")
except TypeError as e:
    print(e)

