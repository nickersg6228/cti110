#CTI-110
#P3HW1-Color Mixer
#Guadalupe Nickerson
#June 18, 2019
#

#Pseudocode
#1.)Declare variables
#primaryColor1=red
#primaryColor2=blue
#2.)Prompt the used for the primary colors
#3.)Combine the primary colors using:
#   primaryColor1+mixed with+primaryColor2 = mixedColor
#4.)Display the mixed colors

primaryColor1= input("Please enter primary color 1: ")
primaryColor2= input("Please enter primary color 2: ")
print()
if (primaryColor1 == "red" and primaryColor2 == "blue")or\
   (primaryColor1 == "blue" and primaryColor2 == "red"):
    print(primaryColor1 + " mixed with " + primaryColor2 + " is purple ")
elif (primaryColor1 == "red" and primaryColor2 == "yellow")or\
     (primaryColor1 == "yellow" and primaryColor2 == "red"):
    print(primaryColor1 + " mixed with " + primaryColor2 + " is orange ")
elif (primaryColor1 == "blue" and primaryColor2 == "yellow")or\
     (primaryColor1 == "yellow" and primaryColor2 == "blue"):
    print(primaryColor1 + " mixed with " + primaryColor2 + " is green ")
      
