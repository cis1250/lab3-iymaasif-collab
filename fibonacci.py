#!/usr/bin/env python3
while True
try: 
  # prompt user for numberof terms
  n=int(input("Enter the number of Fibonacci terms you want: ")) 

if n<=0:
  print("Please enter a positive integer")

else: 
  break
except ValueError: 
print("Invalid input, Please enter a positive integer")
#generate the fibonacci sequence 
a,b =0,1
print("Fibonacci sequence up to {n} terms:")

for_in range(n):
  print(a, end=" ")
  a, b = b, a + b

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
