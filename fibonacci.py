#!/usr/bin/env python3

while True:
    # prompt user for number of terms
    user_input = input("Enter the number of Fibonacci terms you want: ")

    # check if input is digits only
    if user_input.isdigit():
        n = int(user_input)

        if n <= 0:
            print("Please enter a positive integer")
        else:
            break
    else:
        print("Invalid input, please enter a positive integer")

# generate the fibonacci sequence 
a, b = 0, 1
print(f"Fibonacci sequence up to {n} terms:")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()  # moves to a new line after printing

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
