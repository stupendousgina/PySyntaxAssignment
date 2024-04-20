'''Arithmetic Operations in Daily Life''' 

#Task 1: Grocery Store Math. Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic

bread, peanut_butter, jelly = 1.25, 1.25, 1.50

total_cost = bread + peanut_butter + jelly

print(total_cost)

#Task 2: Bank Interest. If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year. So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700.

amount_in_savings = 10000
yearly_intrest_rate = .07

amount_in_savings += (amount_in_savings * yearly_intrest_rate)

print(amount_in_savings)