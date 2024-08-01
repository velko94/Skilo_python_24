# Problem 0:
# Write a program that takes an integer input from the user and checks if it's odd or even.
# Use an if-else statement to print
# the result.
# user_number = int(input("enter any number to test if it is odd or even: "))
#
# if (user_number %2) ==0:
#     print("Number is even")
# else:
#     print("Number is odd")
# Problem 1:
# Write a Python program to find the sum of all even numbers from 1 to 100 using a loop. Make use of control
# flow constructs
# like the for loop and conditional statements.
# starting_number = 1
# even_number = 0
# while starting_number <= 100:
#     starting_number += 1
#     print(starting_number)
#     if starting_number % 2 == 0:
#         even_number = starting_number + even_number
# print(even_number)

# Problem 2:
# Write a Python script that prompts the user in the console a simple problem ( how much does 5 + 17 equal to ) until
# the user provides a correct answer.
#
# problem = 5 + 17
# user_input = int(input("what does 15+17 equal to ", ))
#
# while user_input != problem:
#     user_input = int(input("what does 15+17 equal to ", ))
#
#     if user_input == problem:
#         print("Good")
#         break

# Problem 3:
# Write a Python script that iterates over the first 1000 numbers and prints "Fizz" if the number is divisible by 3,
# "Buzz" if it's divisible by 5, and "FizzBuzz" if it's divisible by both 3 and 5.
# number = int(0)
# while number < 1000:
#     number += 1
#     print(number)
#     if number % 3 == 0:
#         print('fizzy')
#     elif number % 5 == 0:
#         print('buzzy')
#     if number %3==0  and number%5 == 0:
#          print("fizzybuzzy")
# Problem 4:
# Design a Python program that simulates a simple guessing game.
# The program should generate a random number between 1 and 100 and ask the user to guess it.
# Provide hints like "Too high" or "Too low" until the user guesses the correct number. Use a while loop for this game.

# import random
# secret_number = random.randint(1,100)
# print(secret_number)
# user_guess = -1
# while user_guess != secret_number:
#     user_guess = input("Enter your guess: ")
#     guess = int(user_guess)
#     if guess < secret_number:
#         print("Too low, try again.")
#     elif guess > secret_number:
#         print("Too high, try again.")
#     else:
#         print(f"Congratulations! You guessed the number {secret_number} correctly!")
#         break

# Problem 5:
# Modify problem 2 so that every time the user is prompted the problem is different.
# Think of a way to design that and come up with a proper solution for that.

# problem= 0
# user_input = int(input("what does the problem equal to ", ))
#
# while user_input != problem:
#     import random
#     a = random.randint(1, 5)
#     b = random.randint(5, 10)
#     problem = a + b
#     print(f"the solution is", + problem)
#     user_input = int(input("what does problem equal to ", ))
#
#     if user_input == problem:
#         print("Good")
#         break

# Problem 6:
# Write a Python program that takes an integer input from the user and prints the multiplication table
# for that number from 1 to 10 using a for loop.
# num2 = int(input("Display multiplication table of? "))
# for num1 in range(1, 11):
#    print(num2, 'x', num1, '=', num2*num1)

# Problem 7:
# Create a Python program that checks if a given integer is a prime number.
# Use a for loop to iterate through possible divisors and use an if-else statement to determine if it's prime.

# user_input = int(input("Enter a number", ))
# flag = False
# if user_input == 1:
#     print(user_input, "is not a prime number")
# elif user_input > 1:
#     # check for factors
#     for i in range(2, user_input):
#         if (user_input % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break
#
#     # check if flag is True
#     if flag:
#         print(user_input, "is not a prime number")
#     else:
#         print(user_input, "is a prime number")

# Problem 8: Pattern Printing
# Write a program that takes an integer 'n' as input and prints the following pattern using nested for loops:
# Expected output for input “5”:
# n = 5
# for i in range(n):
#    for j in range(i):
#        print(range(n))
# 1
# 12
# 123
# 1234
#  12345
