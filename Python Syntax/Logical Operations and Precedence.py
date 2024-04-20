''' Exploring Logical Operations and Precedence '''

#Task 1: Validating Calculations. Calculate the value of a particular arithmetic expression twice: once normally, and once using parentheses. Compare the two results to see if they match.

a = 1 + 2 * 3
b = (1 + 2) * 3

print("Value without parentheses:", a)
print("Value with parenthese:", b)


#Task 2: Mix and Match. Combine arithmetic (+), logical (or), and comparison (>) operators in a single expression and predict the outcome. Then, compute the expression to see if the prediction was correct.

x = 1
y = 2
z = 10

if z > (x + y) or (x * y): 
    print("z is greater than x and y") 

