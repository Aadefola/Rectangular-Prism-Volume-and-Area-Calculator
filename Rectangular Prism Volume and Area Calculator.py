# Rectangular Prism Volume and Area Calculator (Can also be used to find the area of a rectangle)
length = float(input("Enter the length of the rectangle or Rectangular Prism: "))
width = float(input("Type the width of the rectangule or Rectangular Prism: "))
area = length * width # use * for multiplication
print(f"The rounded area is {round(area)}cm^2") # this will round to a whole number, adjustments can be made if the 
#user would like to specifiy how many decimal places they want
print(f"The area is {area}cm^2")

length = float(input("Enter the length of the Rectangular Prism: "))
width = float(input("Type the width of the Rectangular Prism: "))
height = float(input("Type the height of the Rectangular Prism: "))
volume = length * width * height # use * for multiplication
print(f"The rounded volume is {round(volume)}cm^3") # this will round to a whole number, adjustments can be made if the 
#user would like to specifiy how many decimal places they want
print(f"The volume is {volume}cm^3")