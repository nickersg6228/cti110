#This program will calculate the number of calories burned.
#June 25, 2019
#CTI-110 P4HW1- Calories Burned
#Guadalupe Nickerson

        ##Pseudocode##
#1.)Declare Variables
#   1min=5cal
#2.)Prompt the user for the time in treadmill:
#    print int(input("How long did you run for?"))
#3.)Calculate how many calories where burned
#   10 min=50cal
#   15 min=75cal
#   20 min=100cal
#   25 min=125cal
#   30 min=150cal
#4.)Dispay the number of calories burned in a loop

caloriesBurnedPerMinute=5

for numberOfMinutes in range(10, 31, 5):
    numberOfCaloriesBurned = numberOfMinutes * caloriesBurnedPerMinute
    print ("You will burn", numberOfCaloriesBurned,"in", numberOfMinutes)
    
