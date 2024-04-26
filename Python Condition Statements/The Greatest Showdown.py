'''The Greatest Showdown'''

# Objective: Harness the power of conditional statements to compare and determine values.

# Task 1: Identify the Greatest. Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.

print("Think of three numbers!")

number_1, number_2, number_3 = int(input("Enter your first number: ")), int(input("Enter your second number: ")), int(input("Enter your third number: "))

if number_1 > number_2 and number_1 > number_3:
    print(f"Number {number_1} is the greatest number.")
elif number_2 > number_1 and number_2 > number_3:
    print(f"Number {number_2} is the greatest number.")
elif number_3 > number_1 and number_3 > number_2:
    print(f"Number {number_3} is the greatest number.")

# Task 2: Identify the Smallest. Extend your program from Task 1 to also determine the smallest number among the three and print it out.
    
if number_1 < number_2 and number_1 < number_3:
    print(f"Number {number_1} is the smallest number.")
elif number_2 < number_1 and number_2 < number_3:
    print(f"Number {number_2} is the smallest number.")
elif number_3 < number_1 and number_3 < number_2:
    print(f"Number {number_3} is the smallest number.")

# Task 3: Equality Check. Enhance your program to handle cases where two or all of the numbers are equal. The program should display appropriate messages like "Two numbers are equal and the largest" or "All numbers are equal".
    
if number_1 == number_2 == number_3:
    print("All numbers are equal.")

# Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4. There are two numbers equal to each other." Printing out which numbers are equal would be a great added bonus.

if number_3 > number_2 and number_1 == number_2:
    print(f"The smallest number is {number_1}. The largest number is {number_3}. The first and second number equal to each other.")


