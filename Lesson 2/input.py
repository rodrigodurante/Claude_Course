# LESSON 2 - INPUT AND TYPE CONVERSION

name = input("What is your name? ")

print("Hello,", name, "!")

age = input("What is your age? ")
print(type(age))
age = int(age)

print("Your name is ", name, "and you are ", age, "years old")
print(type(age))

# input() always returns text (str), even if you type a number.

# Then I converted variable 'age' from str to int, by doing the """ age = int(age) """
