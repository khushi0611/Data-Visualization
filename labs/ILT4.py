# Assignment:
# # 1. Write a Python program to sum all the items in a list.
def sum_list(items):
    return sum(items)

items = [1, 2, 3, 4, 5]
print(f"Sum of the list: {sum_list(items)}")



# 2. Write a Python program to get the largest and smallest number from a list without builtin functions.
def get_max_min(numbers):
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num

numbers = [1, 2, 3, 4, 5]
max_num, min_num = get_max_min(numbers)
print(f"Largest number: {max_num}")
print(f"Smallest number: {min_num}")



# 3. Write a Python program to find duplicate values from a list and display those.
def find_duplicates(lst):
    duplicates = []
    seen = set()
    for item in lst:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

lst = [1, 2, 3, 4, 5, 1, 2, 3]
print(f"Duplicate values: {find_duplicates(lst)}")



# 4. Write a Python program to split a given list into two parts where the length of the first part of the list is given.
# Original list: [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list: 3
# Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1])
def split_list(lst, length_first_part):
    return lst[:length_first_part], lst[length_first_part:]

original_list = [1, 1, 2, 3, 4, 4, 5, 1]
first_part_length = 3
first_part, second_part = split_list(original_list, first_part_length)
print(f"Splitted list: {first_part}, {second_part}")



# 5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
# Original list: ['red', 'green', 'white', 'black']
def traverse_reverse_with_index(lst):
    for index in range(len(lst) - 1, -1, -1):
        print(f"Index: {index}, Element: {lst[index]}")

original_list = ['red', 'green', 'white', 'black']
print("Traverse in reverse order with index:")
traverse_reverse_with_index(original_list)



# Assignment:
# 1. Write a Python program and calculate the mean of the below dictionary.
# test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
# Output: 6.2
def calculate_mean(dictionary):
    values = dictionary.values()
    return sum(values) / len(values)

test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
print(f"Mean of the dictionary: {calculate_mean(test_dict)}")



# 2. Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary: dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}
# Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def concatenate_dicts(*dicts):
    result = {}
    for dictionary in dicts:
        result.update(dictionary)
    return result

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
concatenated_dict = concatenate_dicts(dic1, dic2, dic3)
print(f"Concatenated dictionary: {concatenated_dict}")



# 3. Write a Python program to get the key, value and item in a dictionary.
# input: dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Output:
# Key 	Value
# 1	    10
# 2	    20
# 3	    30
# 4	    40
# 5	    50
# 6	    60
def display_dict_items(dictionary):
    print("Key\tValue")
    for key, value in dictionary.items():
        print(f"{key}\t{value}")

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Dictionary items:")
display_dict_items(dict_num)



# 4. Write a Python program to get the key, value and item in a dictionary.
# Input: input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
# Output: dict with empty items Dropped : {1:10,2:20,4:40,6:60}
def remove_empty_items(dictionary):
    return {k: v for k, v in dictionary.items() if v is not None}

input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
cleaned_dict = remove_empty_items(input_dict)
print(f"Dict with empty items dropped: {cleaned_dict}")


# Assignment:
# 1. Write a Python program to find the number of times 4 appears in the tuple.
# Input: tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
# Output: 3
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
count_4 = tuplex.count(4)
print(f"Number of times 4 appears in the tuple: {count_4}")



# 2. Write a Python program to convert a list to a tuple.
# Input: listx = [5, 10, 7, 4, 15, 3]
# Output: (5, 10, 7, 4, 15, 3)
listx = [5, 10, 7, 4, 15, 3]
tuplex = tuple(listx)
print(f"Converted tuple: {tuplex}")



# 3. Write a Python program to calculate the sum of the numbers in a given tuple.
# Input: tuples_list = [(1, 2), (3, 4), (5, 6)]
# Output: sum of tuple is : 21
tuples_list = [(1, 2), (3, 4), (5, 6)]
sum_of_tuples = sum(sum(t) for t in tuples_list)
print(f"Sum of the tuple is: {sum_of_tuples}")



# 4. Write a python program and iterate the given tuples
# Input:
# employee1 = ("John Doe", 101, "Human Resources", 60000)
# employee2 = ("Alice Smith", 102, "Marketing", 55000)
# employee3 = ("Bob Johnson", 103, "Engineering", 75000)
# Output:
# Employee Records :
# Name : John Doe
# Employee ID : 101
# Department : Human Resources
# Salary	:  60000
# Name : Alice Smith
# Employee ID : 102
# Department :Marketing
# Salary	:  55000
# Name : Bob Johnson
# Employee ID : 103
# Department : Engineering
# Salary	:  75000
def display_employee_records(*employees):
    print("Employee Records:")
    for emp in employees:
        print(f"Name: {emp[0]}")
        print(f"Employee ID: {emp[1]}")
        print(f"Department: {emp[2]}")
        print(f"Salary: {emp[3]}\n")

employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)
display_employee_records(employee1, employee2, employee3)



# Assignment:
# 1. Write a Python program to Get Only unique items from two sets.
# Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70}
# Output: {70, 40, 10, 50, 20, 60, 30}
def unique_items_from_sets(set1, set2):
    return set1.symmetric_difference(set2)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_items = unique_items_from_sets(set1, set2)
print(f"Unique items from sets: {unique_items}")



# 2. Write a Python program to Return a set of elements present in Set A or B, but not both.
# Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70}
# Output: {20, 70, 10, 60}
def elements_in_either_but_not_both(set1, set2):
    return set1.symmetric_difference(set2)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = elements_in_either_but_not_both(set1, set2)
print(f"Elements in either set but not both: {result}")



# 3. Write a Python program to Check if two sets have any elements in common. If yes, display the common elements.
# Input: set1 = {10, 20, 30, 40, 50} set2 = {60, 70, 80, 90, 10}
# Output: {10}
def common_elements(set1, set2):
    return set1.intersection(set2)

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
common = common_elements(set1, set2)
print(f"Common elements: {common}")



# 4. Write a Python program to Remove items from set1 that are not common to both set1 and set2.
# Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70}
# Output: {30, 40, 50}
def remove_non_common_items(set1, set2):
    return set1.intersection(set2)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
common_items = remove_non_common_items(set1, set2)
print(f"Items common to both sets: {common_items}")

