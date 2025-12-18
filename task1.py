#Given variables
party_pizza_mini = 14
large = 8
medium = 6
people = 6 # friends

#Do Not use crtl+A to select code.  Only copy the code below this line.
#------------------------------------------------------------------------------------------------
slices = party_pizza_mini + large + medium
print(f"Total number of slices: {slices}")

people = people + 1
share = slices//people
leftover = slices % people
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftover}")

people = people + 2
share = slices//people
leftover = slices % people
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftover}")


slices += party_pizza_mini
share = slices//people
leftover = slices % people
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftover}")
print("...for Mr. Hollow Leg")
