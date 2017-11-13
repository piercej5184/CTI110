# CTI-110 
# M2HW2 - Tip Tax Total 
# Jamire Pierce
# 9/11/2017

foodCost = int(input("Enter the charge for the food:"))

tipAmount = .18 * foodCost
print('The tip amount is $', format(tipAmount, '.2f'))

salesTax = .07 * foodCost
print('The sales tax is $', format(salesTax, '.2f'))


total_cost = foodCost + tipAmount + salesTax


print('Your total cost is $', format(total_cost,'.2f'))
