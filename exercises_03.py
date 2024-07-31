# Exercise 1: Online Shopping Discount

# Given a variable `total_amount` representing the total amount in the shopping cart,
# write a program that prints a discount message if the total amount is over $100,
# and always prints a thank you message.

# total_amount = 110  # Fill in the total amount here
#
# if total_amount > 100:
#     print("Great you get a discount")
# else:
#     print("If you add more you can get a discount")
# print("Thank you for shopping")
# Exercise 2: Temperature Checker
# Given a variable `temperature` representing the current temperature in Celsius,
# write a program that prints "Warm" if the temperature is greater than or equal to 25 degrees Celsius,
# otherwise print "Cool".

# temperature = 28  # Fill in the temperature here
# if temperature>= 25:
#     print("warm")
# else:
#     print("its cool")


# Exercise 3: Time of the Day

# Given a variable `hour` representing the current hour (in 24-hour format),
# write a program that prints "Good Morning" if the hour is before 12 (12 inclusive),
# "Good Afternoon" if the hour is between 12 and 17 (17 inclusive),
# and "Good Evening" if the hour is after 17.
#
# hour = 35  # Fill in the hour here
#
# if hour <= 12:
#     print("Good morning")
# elif hour <= 17:
#     print("Good afternoon")
#
# else:
#     print("Good evening")

# Exercise 4: Secret Message

# Given a variable `message` representing a secret message,
# write a program that prints "Message found" if the message is not empty,
# otherwise print "No message".
# message = ""  # Fill in the message here
# if message != "":
#     print("Message Found")
# else:
#     print("No message")


# Exercise 5: List Iteration
# You have a list of fruits. Write a program that iterates over each fruit in the list and prints each fruit's name.
# fruits = ["Apple", "Banana", "Orange", "Grape", "Watermelon"]
# for fruit in fruits:
#     print(fruit)


# Exercise 6: Range Iteration
# Write a program that prints all the even numbers from 1 to 20 using a for loop and the range() function.
# for number in range(0, 21):
#     if number % 2 == 0:
#         print(number)


# Exercise 7: While Loop
# Write a program using a while loop to find the sum of all numbers from 1 to 100.
# a = 1
# number_sum = 0
# while number_sum <= 100:
#     a += 1
#     number_sumary = number_sum + a
#
# print(number_sumary)

# Exercise 8: Number of Friends

# Write a program that asks how many friends you have and then asks for each of their names.
# num_friends = int(input("how many "))
# list_of_friends = []
#
# for friend in range (0, num_friends):
#     friend_name = str(input(f"what are theyr names {friend + 1} "))
#     list_of_friends.append(friend_name)
# print(f"your friend are {list_of_friends}")

# Exercise 9: Guess the Number
# Write a program that has a number and keeps asking the user to input a number until the user guesses it.
# secret_number = 42
# user_guess = -1
#
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
# Exercise 10: Multiplication Table

# # Generate the multiplication table for the numbers 1 to 9.
# num2 = int(input("Display multiplication table of? "))
# for num1 in range(1, 10):
#    print(num2, 'x', num1, '=', num2*num1)

# Exercise 11: continue

# # Do the same as in Exercise 6 but do not print the number 10. Use `continue` do achieve this
# for num in range(0, 21):
#     if num != 10:
#         print(num)
#     elif num == 10:
#         continue

# Exercise 12: Password Checker

# Write a program that asks the user to enter a password. If the password is correct, print a message saying
# "Access granted" and end the program. If the user enters the wrong password three times, print "Access denied" and
# end the program..
#
# correct_password = "learnpythonwithskillo"
# user_input = str(input("enter you password ", ))
# user_atempts = 1
#
# while user_atempts < 4:
#     if user_atempts <= 3 and user_input == correct_password:
#         print("Access Granted")
#         break
#     elif user_atempts < 3 and user_input != correct_password:
#         print("Try again")
#         user_atempts += 1
#         user_input = str(input("enter you password ", ))
#         pass
#     else:
#         print("Account is locked")
#         break
