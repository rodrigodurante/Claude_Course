# Lesson 2 - Exercise 5

# Run Exercise 2 with a letter instead of a number, to cause Error, then explain the error in a comment

number_one = input("Type the first number: ")
number_one = int(number_one)

number_two = input("Type the second number: ")
number_two = int(number_two)

sum = number_one + number_two

print(sum)

# ValueError: Invalid literal for int() with base 10: 'r'. I typed a letter instead of a number and Python couldn't read it
# because once I wrote number_one = int(number_one) I converted it to Integer, the variable will only read if
# the typed information was integer numbers, not even float.
