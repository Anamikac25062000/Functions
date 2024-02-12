#1)Write a Python function that calculates the factorial of a given integer. Demonstrate how to call this function with an example.

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# example = 5
# result = factorial(example)
# print(f"The factorial of {example} is: {result}")



#2)Create a function that takes two arguments, a name and an age, and prints a message like "Hello,   [Name]! You are [Age] years old." Call this function with your name and age as arguments. 

# def greet_person(name, age):
#     print(f"Hello, {name}! You are {age} years old.")
# my_name = "Anamika"
# my_age = 23
# greet_person(my_name, my_age)



#3)Write a Python function to find the maximum of three numbers. 

# def max_three(n1,n2,n3):
#     if n1>n2>n3:
#         return n1
#     elif n2>n1>n3:
#         return n2
#     else:
#         return n3
# print(max_three(100,20,3))



#4)Write a Python program to reverse a string 

# def rev_str(inp_str):
#     return inp_str[::-1]
# input_value = input("Enter a string: ")
# reversed_string = rev_str(input_value)
# print("Original value:",input_value)
# print("Reversed string:",reversed_string)



#5)Write a Python function that accepts a string and counts the number of upper and lower case letters. 

# def count_letters():
#     user_input = input("Enter a string: ")
#     upper_count = sum(1 for char in user_input if char.isupper())
#     lower_count = sum(1 for char in user_input if char.islower())

#     return upper_count, lower_count
# upper, lower = count_letters()

# print(f"Uppercase count: {upper}")
# print(f"Lowercase count: {lower}")



#6)Write a Python function that takes a number as a parameter and checks whether the number is prime or not.  

# def prime(number):
#     if number <= 1:
#         return False
#     elif number == 2:
#         return True
#     elif number % 2 == 0:
#         return False
#     else:
#         for i in range(3, int(number**0.5) + 1, 2):
#             if number % i == 0:
#                 return False
#         return True
# user_input = int(input("Enter a number: "))

# if prime(user_input):
#     print(f"{user_input} is a prime number.")
# else:
#     print(f"{user_input} is not a prime number.")




#7)Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. 
# Sample Items : green-red-yellow-black-white 
# Expected Result : black-green-red-white-yellow 

# def sort_words(sequence):
#     words = sequence.split('-')
#     sorted_words = sorted(words)
#     sorted_sequence = '-'.join(sorted_words)
#     return sorted_sequence

# input_sequence = "green-red-yellow-black-white"
# result = sort_words(input_sequence)

# print(f"Original Sequence: {input_sequence}")
# print(f"Sorted Sequence: {result}")



#8)Define a function that accepts 2 values and return its sum, subtraction and multiplication. Using 4 types of functions based on arguments and return type. 

#a)Function  with arguments and with return type
# def coperations(v1, v2):
#     sum = v1 + v2
#     subtraction = v1 - v2
#     multiplication = v1 * v2
#     return sum, subtraction, multiplication
# v1 = 10
# v2 = 5
# sum, subtraction, multiplication = calculate(v1, v2)
# print(f"Sum: {sum}")
# print(f"Subtraction: {subtraction}")
# print(f"Multiplication: {multiplication}")

# # b)Function  with arguments and without return type
# def operations(a, b):
#     sum_result = a + b
#     sub_result = a - b
#     mul_result = a * b

#     print(f"Sum: {sum}")
#     print(f"Subtraction: {sub}")
#     print(f"Multiplication: {mul}")
# value1 = 10
# value2 = 5
# operations(v1, v2)

# # c)Function without default arguments and return value:
# def operations():
#     v1 = float(input("Enter the first value: "))
#     v2 = float(input("Enter the second value: "))
    
#     addition = v1 + v2
#     subtraction = v1 - v2
#     multiplication = v1 * v2
    
#     return addition, subtraction, multiplication
# add, sub, mul = operations()
# print("Addition:", add)
# print("Subtraction:", sub)
# print("Multiplication:", mul)

# # d)without argument without return type

# def operations():
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     print("Sum:", num1 + num2)
#     print("Subtraction:", num1 - num2)
#     print("Multiplication:", num1 * num2)

# perform_operations()


#9)Define a function that accepts roll number and returns whether the student is present or absent.
 
# def attendance(roll_number, present_roll_numbers):
#     if roll_number in present_roll_numbers:
#         return "Present"
#     else:
#         return "Absent"

# input_roll_number = int(input("Enter your roll number: "))

# present_roll_numbers = [101, 102, 103, 104, 105]

# today_attendance = attendance(input_roll_number, present_roll_numbers)

# print(f"Student with Roll Number {input_roll_number} is {today_attendance}")

#10)Define a function that accepts lowercase words and returns uppercase words. 

# def convert_to_uppercase(words):
#     return [word.upper() for word in words]

# user_input = input("Enter lowercase words: ")

# lowercase_words = user_input.split()

# uppercase_words = convert_to_uppercase(lowercase_words)

# print(f"Original Words: {lowercase_words}")
# print(f"Uppercase Words: {uppercase_words}")

