#input the length and width of rectangle 1
#input the length and width of rectangle 2
#calculate the area of rectangle 1
#calculate the area of rectangle 2
#outcomes:
# rectangle 1 will have the greatest area
# rectangle 2 will have the greatest area
# both rectangle have the same area
# if area1> area2
#display "rectangle 1 has the greatest are"
# else if area2> area1
#display "rectangle 2 has the greatest are"
#else
#display "both rectangles have the same are"

#Get dimensions of rectangle 1.
length1 = int(input("Enter the length of rectangle 1: "))
width1 = int(input("Enter the width of rectangle 1: "))

#Get dimensions of rectangle 2.
length2 = int(input("Enter the length of rectangle 2: "))
width2 = int(input("Enter the width of rectangle 2: "))

#Calculate the areas fo the rectangle.
area1 = length1 * width1
area2 = length2 * width2

#Determine which has the greater area.

if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
     print('Rectangle 2 has the greater area.')
else:
    print ('Both have the same area.')

