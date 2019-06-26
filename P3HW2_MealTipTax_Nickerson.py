#CTI-110
#P3HW2-MealTipTax
#Guadalupe Nickerson
#June 18, 2019
#
#Pseudocode
#1.) Declare variables
#    meal= 0.0
#    tax= .07
#    tipPercentage = percentage/100
#    total= 0.0
#2.)Prompt the user for the bill and tip amount
#3.) Calculate the total using:
#    total= bill * .7 * tip
#4.) Display the total amount for their bill
#    "Your total is:"






meal = float(input("How much was your bill? "))
tax = meal + (meal * .07)
tipPercentage = float(input("How much would you like to tip? "))
total = tax + (tax * tipPercentage/100)
print ("Your total with tax and tip is:$%.2f" % total)



##
##meal = float(input("How much was your bill?"))
##tax = meal + (meal * .07)
##percentage = float(input("How much would you like to tip?"))
##tip_percentage = tax + (meal * percentage/100)
##total = meal + tip_percentage
##print ("Your grand total is:$  %.2f" % total)
