#Python code to calculates the factorial of a number
# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum
sum_result = num1 + num2

# Display the result
print(f"The sum of {num1} and {num2} is {sum_result}")

# Check if a number is prime
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# Code  to get a list of all the prime numbers between 1 and 100

def is_prime(number):
  for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
      return False
  return True


prime_numbers = []
for number in range(1, 101):
  if is_prime(number):
    prime_numbers.append(number)

print(prime_numbers)
