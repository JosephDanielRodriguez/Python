# Hello World Program
# Created by Joseph Rodriguez
# Who wants to be in infosec but doesn't know Python for some reason

print("Hello World!")
print("Guess who's learning Python finally!")
print("With Python, I can now do so much more than just Java ;)")
print()
print("** Simple Math **")

# num variables
num1 = 54
num2 = 25

# adds those numbers
sum = num1 + num2

# displays the two numbers and sum
print()
print('The first number is {0}' .format(num1))
print('The second number is {0}' .format(num2))
print()
print('The sum of {0} and {1} is equal to {2}' .format(num1, num2, sum))
print()

print("** You choose the numbers **")
print()

# prompts user for numbers
num1 = input('Enter a number: ')
num2 = input('Enter another number: ')

# adds those numbers
sum = float(num1) + float(num2)

# displays the sum
print()
print('The sum of {0} and {1} is equal to {2}' .format(num1, num2, sum))
print()

print("** More input practice **")

print()
print("I want to make you a quick profile card. I'm going to ask you a few questions")
name = input('What is your full name?: ')
age = input('What is your age?: ')
favColor = input('What is your favorite color?: ')
favFood = input('What is your favorite food?: ')
print("Great! Here's what we got!")

print()
print("Name: {0}" .format(name))
print("Age: {0}" .format(age))
print("Favorite Color: {0}" .format(favColor))
print("Favorite Food: {0}" .format(favFood))
print()

print("Python is fun. I will keep learning more of it :D")
