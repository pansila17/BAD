#Code to takes a length in meters as input from the user and converts it to centimeters
# Input length in meters from the user
meters = float(input("Enter length in meters: "))

# Convert meters to centimeters
centimeters = meters * 100

# Print the result
print(f"{meters} meters is equal to {centimeters} centimeters.")


# code to convert milliliters into liters
# Input from the user in milliliters
milliliters = float(input("Enter the volume in milliliters: "))

# Convert milliliters to liters
liters = milliliters / 1000

# Print the result
print(f"{milliliters} milliliters is equal to {liters} liters.")


# code to calculate the area of a rectangle based on user input for its length and width
# Input from the user for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area = length * width

# Print the result
print(f"The area of the rectangle with length {length} and width {width} is {area}.")

# calculates the square of a number
def square(number):
    return number ** 2

result = square(5)
print("The square of 5 is", result)



