'''Leap Year Explorer''' 

# Objective: Dive deep into the intricacies of the calendar by exploring the concept of leap years.

# Task 1: Leap Year Checker. Write a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and then display an appropriate message. Please note that this is the definition of a leap year: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

# Expected Outcome: If you test the year 1900, is should be False. The year 2000 should be True. The year 2024 should be True

leap_year = int(input("Enter a year to find out if its a leap year: "))

if (leap_year % 400 == 0) and (leap_year % 100 == 0):
    print(f"{leap_year} is a leap year!")
elif (leap_year % 4 == 0) and (leap_year % 100 != 0):
    print(f"{leap_year} is a leap year!")
elif (leap_year % 100 == 0) or (leap_year % 4 != 0):
    print(f"{leap_year} is not leap year.")

